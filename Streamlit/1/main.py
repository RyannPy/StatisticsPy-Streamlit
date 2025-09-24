import streamlit as st
import statistics as stc
import time

st.title("📊 Py Statistics")
st.text("Olah angka dan data kamu!")

# Fungsi
def ratarata(a):
    return sum(a) / len(a)

def terbesar(x):
    return max(x)

def terkecil(n):
    return min(n)

def median(data):
    return stc.median(data)

def modus(data):
    return stc.mode(data)  # di Python terbaru "modus" diganti jadi "mode"

def stdev(data):
    return stc.stdev(data)

def range_data(data):
    return max(data) - min(data)


# Main
def main():
    input_str = st.text_input("Masukkan angka (pisahkan dengan spasi):")
    
    if input_str:
        try:
            data = list(map(int, input_str.split()))
            
            if st.button("Olah!"):
                with st.spinner("🔄 Sedang memproses data..."):
                    progress = st.progress(0)
                    for i in range(100):
                        time.sleep(0.01)  # simulasi proses
                        progress.progress(i+1)

                # Hasil perhitungan
                hasil_rata = ratarata(data)
                hasil_terbesar = terbesar(data)
                hasil_terkecil = terkecil(data)
                hasil_median = median(data)
                hasil_modus = modus(data)
                hasil_stdev = stdev(data)
                hasil_range = range_data(data)

                st.success("✅ Data berhasil diolah!")

                # Display hasil (pakai card metric biar rapi)
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Rata-rata", f"{hasil_rata:.2f}")
                    st.metric("Median", f"{hasil_median}")
                    st.metric("Modus", f"{hasil_modus}")

                with col2:
                    st.metric("Terbesar", f"{hasil_terbesar}")
                    st.metric("Terkecil", f"{hasil_terkecil}")

                with col3:
                    st.metric("Stdev", f"{hasil_stdev:.2f}")
                    st.metric("Range", f"{hasil_range}")

        except Exception as e:
            st.error(f"Input salah: {e}")

main()
