# VieTokenizer
This is a new package that supports Vietnamese word segmentation based on deep learning methods. The model architecture we use is a simple bi-lstm network trained on a pre-labeled dataset. For example, the training set: "Tôi tên là Nguyễn Tiến Đạt" and the test set: "Tôi tên là Nguyễn_Tiến_Đạt". The model will predict if serial word is 1 and non-serial is 0, for example, "Tôi tên là Nguyễn Tiến Đạt" will be equivalent to a sequence of numbers with both zero and one being [0, 0, 0, 0, 1, 1]. 

## Installation 🎉
- This repository is tested on python 3.7+ and Tensorflow 2.8+
- VieTokenizer can be installed using pip as follows:
```
pip install vietokenizer 🍰
```
- VieTokenizer can also be installed from source with the following commands: 
```
git clone https://github.com/Nguyendat-bit/VieTokenizer
cd VieTokenizer
pip install -e . 
```
## Usage 🔥
```python
>>> import vietokenizer
>>> tokenizer= vietokenizer.vntokenizer()
>>> tokenizer('Tôi tên là Nguyễn Tiến Đạt, hiện là sinh viên Đại học CN GTVT tại Hà Nội.')
'Tôi tên là Nguyễn_Tiến_Đạt , hiện là sinh_viên Đại_học CN GTVT tại Hà_Nội .'
>>> tokenizer('Kim loại nặng thường được định nghĩa là kim loại có khối lượng riêng, khối lượng nguyên tử hoặc số hiệu nguyên tử lớn.')
'Kim_loại nặng thường được định_nghĩa là kim_loại có khối_lượng riêng , khối_lượng nguyên_tử hoặc số_hiệu nguyên_tử lớn .'
```

## License
[Apache 2.0 License](https://github.com/Nguyendat-bit/VieTokenizer). <br>
Copyright &copy; 2022 [Nguyễn Tiến Đạt](https://github.com/Nguyendat-bit). All rights reserved.
