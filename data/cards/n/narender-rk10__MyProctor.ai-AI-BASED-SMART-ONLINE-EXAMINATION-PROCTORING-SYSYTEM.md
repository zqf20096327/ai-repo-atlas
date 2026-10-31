# narender-rk10/MyProctor.ai-AI-BASED-SMART-ONLINE-EXAMINATION-PROCTORING-SYSYTEM

⭐ 236 · HTML · 推送 2026-10-30 · [GitHub](https://github.com/narender-rk10/MyProctor.ai-AI-BASED-SMART-ONLINE-EXAMINATION-PROCTORING-SYSYTEM) · 个人维护

**AI 在线考试监考系统：人脸识别、视线估计与作弊检测**

基于 Python Flask 与 MySQL 的在线考试监考系统，使用 YOLO、人脸识别与视线估计等 AI 技术。功能覆盖：登录时人脸图像验证与单账号限制；教授端 AI 生成客观/主观题、创建考试、实时监看与查看监考日志、录入成绩并发布结果；学生端参加客观/主观/实操三类考试（支持负分制、随机出题、计算器、20 种编译器/解释器）。监考包括切屏与窗口事件日志、每 5 秒音频频率与图像日志、手机与多人检测、视线/身体姿态估计，禁用复制粘贴截图；VM 与屏幕共享检测仅限桌面端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 人脸识别登录验证与考试中持续核验
- 切窗事件、音频频率（每5秒）、图像日志与手机/多人检测
- 视线估计追踪考生身体与眼球运动
- AI 生成客观/主观题，支持 20 种编程语言实操考试

## 适用场景

- 教育机构开展带自动监考的在线考试
- 考试中检测手机、多人与切屏等作弊行为
- 教授批量生成题目并实时监控考试过程

## 场景标签

`人脸识别` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L56: 3) Detection of Mobile phone.
> L58: 5) Gaze Estimation: Estimating the position of student body & eyes movements.


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `ca3199296136` · [字段定义](../../DATASET.md)*
