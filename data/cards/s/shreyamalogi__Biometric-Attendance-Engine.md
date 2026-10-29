# shreyamalogi/Biometric-Attendance-Engine

⭐ 18 · HTML · MIT · 推送 2026-02-01 · [GitHub](https://github.com/shreyamalogi/Biometric-Attendance-Engine) · 个人维护

**基于人脸识别的实时考勤系统（Flask/OpenCV/HOG/Dlib）**

面向学校等机构的人脸识别考勤 Web 应用：以 HOG 特征编码与 Dlib 68 点关键点检测进行人脸识别，结合 face_recognition 库匹配已训练的人脸编码库。提供三种输入模式：实时摄像头、静态图片批处理、录像回放分析。后端用 Flask 管理视频流，SQLAlchemy/SQLite 存储 Users/Students/Semesters 与考勤记录，Werkzeug 与 Flask-Login 做密码哈希和会话保护，Pandas 生成 CSV 考勤报表，前端为 Bootstrap/Jinja2。安装方式为 pip 依赖加 python main.py 启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HOG 编码 + Dlib 68 点关键点检测的人脸识别管线
- 三种输入模式：实时摄像头/静态图片批处理/录像回放
- SQLAlchemy/SQLite 存储 + Flask-Login 管理员会话保护
- Pandas 自动生成 CSV 考勤报表

## 适用场景

- 课堂实时点名并自动记录考勤到数据库
- 活动后对照片批量核验出席人员
- 从已录制视频中补录考勤

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L29: * **Methodology**: Utilized **HOG (Histogram of Oriented Gradients)** for robust facial feature encoding, ensuring 
> L31: * **Identity Logic**: Integrated `face_recognition` libraries to map detected landmarks against a trained encoding 

## 星数曲线

```mermaid
xychart-beta
    title "shreyamalogi/Biometric-Attendance-Engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f3d51db5e02b` · [字段定义](../../DATASET.md)*
