# MuhammadLutfiMuzakiiVY/Litera-AI-iOS

⭐ 16 · Dart · MIT · 推送 2026-08-25 · [GitHub](https://github.com/MuhammadLutfiMuzakiiVY/Litera-AI-iOS) · [官网](https://github.com/MuhammadLutfiMuzakiiVY/Litera-AI-iOS) · 个人维护

**面向学生/教师/家长的印尼文学阅读自适应学习平台（移动端+后端+AI）**

LITERA-AI 单体仓库，包含 Flutter 移动客户端、FastAPI 异步后端与独立 Python AI 模块，服务于印尼国家阅读素养恢复项目 P-LIDM。学生先做阅读水平诊断测评（初学者/中级/精通），AI 据此生成个性化印尼古典文学阅读路径；阅读中可点按文本获得词汇/修辞释义。AI 机制包括：基于贝叶斯分类的 Knowledge Tracing、按正确率与作答时长实时调整题目难度的 DDA 决策树，以及通过 Gemini API 按 Bloom 分类法自动生成文学测验题。教师可在 Web 仪表盘查看班级成绩分布，家长可接收 AI 阅读指导建议。离线答题经 Hive 本地 outbox 队列批量同步至 PostgreSQL；Redis 用于缓存与 OTP 校验。提供 Docker Compose 部署方案。

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

- 诊断测评+Knowledge Tracing 生成个性化阅读路径
- DDA 算法依据正确率(>85%升/<50%降)与作答时长动态调整题目难度
- Gemini API 按 Bloom 分类法自动生成文学测验题
- Flutter 客户端离线优先：Hive 本地缓存 + outbox 队列批量同步

## 适用场景

- 学生进行阅读水平测评并获得自适应文学阅读与测验
- 教师在仪表盘监测班级学习进度与成绩分布
- 家长接收 AI 生成的家庭阅读指导建议
- 离线环境下答题，联网后自动批量同步学习数据

## 场景标签

 · 领域:教育科技/自适应学习

## 证据(README 行号)

> L14: **LITERA-AI Monorepo** adalah pusat pengembangan kode terpadu yang memuat seluruh infrastruktur aplikasi seluler (m
> L28:  - Berdasarkan hasil asesmen, mesin AI menentukan daftar novel sastra klasik Indonesia yang paling cocok untuk diba
> L102: ## 🤖 5. Modul Kecerdasan Buatan (Predictive AI Engine Detail)

## 星数曲线

```mermaid
xychart-beta
    title "MuhammadLutfiMuzakiiVY/Litera-AI-iOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `61d3693e9756` · [字段定义](../../DATASET.md)*
