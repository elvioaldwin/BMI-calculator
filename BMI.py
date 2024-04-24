import streamlit as st
import matplotlib.pyplot as plt

def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "Makan lebih banyak dan bergizi.", "#3498db"
    elif 18.5 <= bmi < 25:
        return "Normal", "Pertahankan pola makan dan olahraga yang baik.", "#2ecc71"
    elif 25 <= bmi < 30:
        return "Overweight", "Coba kurangi kalori dan tingkatkan aktivitas fisik.", "#f39c12"
    else:
        return "Obese", "Sangat disarankan untuk berkonsultasi dengan dokter atau ahli nutrisi.", "#e74c3c"

def plot_bmi(bmi):
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    values = [18.5, 24.9, 29.9, 40]  # max values for each category
    colors = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c']

    plt.figure(figsize=(8, 4))
    barlist = plt.bar(categories, values, color=colors)
    
    # Highlighting the bar relevant to the user's BMI
    if bmi < 18.5:
        barlist[0].set_alpha(0.5)
    elif bmi < 25:
        barlist[1].set_alpha(0.5)
    elif bmi < 30:
        barlist[2].set_alpha(0.5)
    else:
        barlist[3].set_alpha(0.5)
        
    plt.axhline(y=bmi, color='black', linewidth=2, linestyle='--')
    plt.text(3.5, bmi, f'Your BMI: {bmi:.1f}', verticalalignment='bottom', horizontalalignment='right')
    plt.ylabel('BMI Values')
    plt.title('BMI Categories and Where You Stand')
    plt.tight_layout()

    return plt

def main():
    st.title('Interactive BMI Calculator')
    st.write("### Anggota Kelompok:")
    st.write("""
    1. Elvio
    2. Prameshti
    3. Indana Zulfa
    4. Raden
    5. Nayla Rahma
    """)
    
    st.write("""
    ## Tentang Aplikasi Ini
    Aplikasi ini dibuat untuk memudahkan pengguna dalam menghitung dan memahami nilai BMI (Body Mass Index) mereka. 
    Dengan memasukkan berat dan tinggi badan, aplikasi ini akan menghitung BMI dan memberikan informasi tentang kategori 
    kesehatan yang sesuai dengan BMI tersebut. Aplikasi ini juga menyertakan visualisasi grafik untuk memperjelas 
    posisi BMI pengguna relatif terhadap kategori yang ada.
    """)

    with st.sidebar:
        name = st.text_input("Masukkan nama Anda:")
        weight = st.number_input("Masukkan berat Anda (dalam kg):", min_value=1.0, format="%.2f")
        height = st.number_input("Masukkan tinggi Anda (dalam cm):", min_value=1.0, format="%.2f")
    
    if st.sidebar.button('Hitung BMI'):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            category, advice, color = interpret_bmi(bmi)
            st.success(f'Halo {name}, BMI Anda adalah {bmi:.2f}.')
            st.info(f'Anda berada dalam kategori **{category}**. {advice}', icon="ℹ️")

            fig = plot_bmi(bmi)
            st.pyplot(fig)
        else:
            st.error("Mohon masukkan data yang valid!")

if __name__ == '__main__':
    main()
