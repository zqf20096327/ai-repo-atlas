# MuhammadLutfiMuzakiiVY/Litera-AI-Android

⭐ 16 · Dart · MIT · 推送 2026-08-25 · [GitHub](https://github.com/MuhammadLutfiMuzakiiVY/Litera-AI-Android) · [官网](https://github.com/MuhammadLutfiMuzakiiVY/Litera-AI-Android) · 个人维护

**面向印尼读写能力提升的自适应文学阅读学习 Android 应用（单体仓库）**

LITERA-AI 单体仓库，包含 Flutter 移动客户端、FastAPI 后端与独立 Python AI 模块，服务于学生、教师、家长三类角色的阅读诊断与学习流程。学生先完成初始诊断测验（初学者/中级/高级），AI 据此匹配印尼经典文学作品；阅读中可点击文本获取词汇/修辞释义，章节后进入自适应测验（DDA 按正确率与作答时长动态调难度），并含知识追踪（Knowledge Tracing）与 Gemini API 自动出题。后端使用 PostgreSQL/Redis/SQLAlchemy，移动端为 offline-first 架构（Hive 本地库+离线 outbox 队列，联网后批量同步）。提供 Flutter、pip 与 Docker Compose 三种运行途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 初始诊断测验+个性化阅读路径推荐
- DDA 动态难度调整（依据正确率与作答时长）与贝叶斯知识追踪
- 通过 Gemini API 按 Bloom 分类法自动生成文学测验题目
- offline-first 移动端：Hive 本地缓存与离线 outbox 批量同步

## 适用场景

- 学生进行阅读能力诊断并按等级阅读推荐文学作品
- 阅读中即时获取难词与修辞的上下文释义
- 教师与家长在 dashboard 查看班级成绩分布与 AI 阅读指导建议

## 场景标签

 · 领域:教育科技/读写能力提升

## 证据(README 行号)

> L28:  - Berdasarkan hasil asesmen, mesin AI menentukan daftar novel sastra klasik Indonesia yang paling cocok untuk diba
> L32:  - Setelah menyelesaikan bab membaca, murid mengerjakan kuis. Mesin AI (DDA) memantau akurasi jawaban dan durasi pe
> L52: * **Mesin Pembuat Soal Gemini AI (Gemini AI Quiz Generation Engine)**:

## 星数曲线

```mermaid
xychart-beta
    title "MuhammadLutfiMuzakiiVY/Litera-AI-Android 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `61d3693e9756` · [字段定义](../../DATASET.md)*
