from flask import Flask, request, jsonify
from lunar_python import Lunar, Solar

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert_solar_to_lunar():
    # 获取查询参数中的阴历年月日
    lunar_year = request.args.get('year', type=int)
    lunar_month = request.args.get('month', type=int)
    lunar_day = request.args.get('day', type=int)
    
    if lunar_year and lunar_month and lunar_day:
        # 从请求中获取输入参数
        year = int(request.args.get('year'))
        month = int(request.args.get('month'))
        day = int(request.args.get('day'))
        hour = int(request.args.get('hour'))
        minute = int(request.args.get('minute'))

        # 通过Solar类创建阳历日期
        solar = Solar.fromYmdHms(year, month, day, hour, minute, 0)

        # 将阳历日期转为阴历信息
        lunar = solar.getLunar()

        # 构建返回信息的字典，包含阳历和阴历的信息
        response_data = {
            'solar_year': year,
            'solar_month': month,
            'solar_day': day,
            'solar_hour': hour,
            'solar_minute': minute,
            'lunar_year': lunar.getYear(),
            'lunar_month': lunar.getMonth(),
            'lunar_day': lunar.getDay(),
            'year_ganzhi': lunar.getYearInGanZhiExact(),
            'month_ganzhi': lunar.getMonthInGanZhiExact(),
            'day_ganzhi': lunar.getDayInGanZhi(),
            'hour_ganzhi': lunar.getTimeInGanZhi()
        }
        # 返回JSON格式响应
        return jsonify(response_data)

    else:
        return jsonify({'error': '请提供有效的year、month和day参数'}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)
