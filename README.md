# WRANGLING-SQL-PROJECT
WRANGLING & SQL PROJECT
BY RYAN ARIESTA

REPOSITORY LINK
Project ini menggunakan “Jupyter Notebook” please check my repository link :
https://github.com/Ryan77Ariesta/WRANGLING-SQL-PROJECT

STEP 1 — OBJECTIVE
Mengetahui Product apa yang paling banyak dipesan
Mengetahui total value dari masing-masing Product
Mengetahui Daerah dengan penjualan tertinggi
STEP 2 — DATASET
Dataset yang adalah digunakan diambil dari database “olist.db” yang berisikan 9 tabel: [(‘olist_order_customer_dataset’,), (‘olist_order_dataset’,), (‘olist_order_reviews_dataset’,), (‘olist_order_payments_dataset’,), (‘olist_order_items_dataset’,), (‘olist_products_dataset’,), (‘olist_sellers_dataset’,), (‘olist_geolocation_dataset’,), (‘product_category_name_translation’,)]

Dalam analisa ini, ada 5 tabel yang digunakan yaitu olist_order_items_dataset (tabel item), olist_products_dataset (tabel Product), olist_order_payments_datase (tabel payments), olist_order_dataset (tabel order), olist_order_customer_dataset (tabel customer).

1.DATASET olist_order_items_dataset (tabel item)


order_id = kode unik dari setiap data order
order_item_id =nomor urut untuk mengidentifikasi jumlah barang yang masuk dalam urutan yang sama
product_id = kode unik dari setiap product
seller_id = kode unit dari setiap penjual
shipping_limit_date = menunjukkan batas tanggal pengiriman pesanan
price = harga item
freight_value = nilai dari pengiriman (ongkos kirim)

2.DATASET olist_products_dataset (tabel Product)


product_id= kode unik dari setiap product
product_category_name= nama dari kategori product
product_name_lenght= jumlah huruf / panjang nama product
product_description_lenght= jumlah huruf / panjang nama product deskripsi
product_photos_qty= jumlah dari foto product yang di publikasikan
product_weight_g= berat product dalam gram
product_length_cm= panjang product dalam cm
product_height_cm= tinggi product dalam cm
product_width_cm= lebar product dalam cm

3.DATASET olist_order_payments_datase (tabel payments)


order_id = kode unik dari setiap data order
payment_sequential =nomor urut untuk mengidentifikasi pembayaran
payment_type=jenis pembayaran
payment_installments = jumlah pembayaran
payment_values = nilai pembayaran

4.DATASET olist_order_dataset (tabel order)


order_id= kode unik dari setiap data order
customer_id= kode unit dari setiap konsumen
order_status= status order referensi
order_purchase_timestamp= stempel waktu pembelian
order_approved_at= stempel waktu persetujuan pembayaran
order_delivered_carrier_date= stempel waktu pengiriman pesanan
order_delivered_customer_date= tanggal pengiriman pesanan yang sebenarnya kepada pelanggan
order_estimated_delivery_date= perkiraan tanggal pengiriman yang diinformasikan kepada pelanggan pada saat pembelian

5.DATASET olist_order_customer_dataset (tabel customer)


customer_id= kode unik dari setiap konsumen
customer_unique_id= kode unit dari setiap transaksi konsumen
customer_zip_code_preflix= kode pos konsumen
customer_city= kota asal konsumen
customer_state= state konsumen

STEP 3 — EXPLORASI DAN PENGOLAHAN DATA
Tabel order: terdapat missing value di beberapa kolom dengan missing value terbanyak sebanyak 2965 value, namun tidak pada kolom yang akan kita gunakan.
Tabel items: tidak terdapat missing value maupun duplikasi data


Tabel products: terdapat missing value di beberapa kolom dengan missing value terbanyak sebanyak 610 value. Terdapat juga inkonsistensi di kolom product_category_name.


PEMROSESAN DATA

Menggabungkan semua data yang diperlukan untuk visualisasi dan pembacaan data yang lebih baik

menggabungkan data untuk OBJECTIVE 1 ( Mengetahui Product apa yang paling banyak di pesan ) dengan menggabungkan table item dengan tabel product lalu menghitung jumlah order yang ada untuk mengetahui total pemesanan di masing masing product



lalu melakukan visualisasi untuk mempermudah pembacaan data yang ada



menggabungkan data untuk OBJECTIVE 2 ( Mengetahui total value dari masing-masing Product ) menggabungkan atara tabel item tabel prodyct dengan tabel payment lalu mensort nya berdasarkat product category dengan payment value untuk mengetahui value untuk masing masing product


lalu melakukan visualisasi untuk mempermudah pembacaan data yang ada



menggabungkan data untuk OBJECTIVE 3 ( Mengetahui Daerah dengan penjualan tertinggi ) menggabungkan data order dengan data customer untuk mengetahui jumlah order masing masing customer berdasarkan customer_state



lalu melakukan visualisasi untuk mempermudah pembacaan data yang ada



STEP 4 — HASIL ANALISA
Mengetahui Product apa yang paling banyak dipesan
Dari data yang ada dapat diketahui bahwa #top5 product yang paling banyak di pesan adalah camma_messa-banho, Beleza_saude, Esporte_lazer, Moveis_decoracao, Informatica_acessorios. dari data ini kita bisa melakukan segmentasi product dan memetakan product apa saja yang perlu kita siapkan secara berkala untuk memenuh pasar agar tidak terjadi permintaan yang tinggi tetapi supply rendah.
Mengetahui total value dari masing-masing Product
Dari data yang ada dapat diketahui bahwa #top5 product yang paling menguntungkan adalah camma_messa-banho, Beleza_saude, Esporte_lazer, Moveis_decoracao, Informatica_acessorios. bisa disimpulkan bahwa dengan kita memperbanyak penjualan 5 product ini kita dapat menghasilkan profitability yang baik
Mengetahui Daerah dengan penjualan tertinggi
Dari data yang ada dapat diketahui bahwa #top5 daerah berdasarkan customer_state yang paling banyak memesan adalah SP , RJ, MG, RS, PR, dari sini kita bisa memetakan area mana yang perlu kita jaga secara tingkat pemesanananya cukup tinggi
STEP 5 — PENUTUP
Tentunya analisis masih harus diperdalam lagi dengan insight-insight yang lebih jelas dan lebih detail untuk perkembangan bisnis dan strategy pemasaran serta penjualan. Misalnya, menganalisis apakah produk yang dipesan ini pasti sampai ke pelanggan, lokasi toko yang paling laris menjual produk tertentu, dan sebagainya. Hal ini bisa menjadi eksplorasi yang baik di analisis berikutnya.





