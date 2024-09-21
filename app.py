from flask import Flask, request, jsonify
from lunar_python import Lunar

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert_lunar_to_solar():
    # 获取查询参数中的阴历年月日
    lunar_year = request.args.get('year', type=int)
    lunar_month = request.args.get('month', type=int)
    lunar_day = request.args.get('day', type=int)
    
    if lunar_year and lunar_month and lunar_day:
        # 使用提供的阴历年月日初始化
        lunar = Lunar.fromYmd(lunar_year, lunar_month, lunar_day)
        
        # 返回阴历和对应的阳历
        return jsonify({
            'lunar': lunar.toFullString(),
            'solar': lunar.getSolar().toFullString()
        })
    else:
        return jsonify({'error': '请提供有效的year、month和day参数'}), 400

if __name__ == '__main__':
    app.run(debug=True)
