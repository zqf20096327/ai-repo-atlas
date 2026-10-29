# RakeshBabuGajula/Exam_Intellect

⭐ 18 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/RakeshBabuGajula/Exam_Intellect) · 个人维护

**给教育机构的 AI 考试监考与补救辅导多智能体系统**

面向在线考试监考场景的多智能体系统：Proctor Agent 用 OpenCV 在 30 FPS 下做人脸存在、注视偏移与多重人脸检测（IoU 去重过滤），配合麦克风做背景语音关键词检测；30 秒遥测包发送至 Google Gemini 2.0 Flash 做行为风险分类。考后由 Tutor Agent 生成 4 周个性化补习计划与讲解内容，Communication Agent 通过 SMTP 邮件与 webhook 派发分级事件报告。提供 Streamlit 监控面板、SQLite 持久化与 CLI 三种运行方式，需自备 GEMINI/OPENAI API key、摄像头与麦克风。

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

- 30 FPS OpenCV 实时监考：人脸/注视偏移/离席检测，IoU 过滤重复人脸框
- 语音异常检测：环境噪声校准下识别低语关键词
- 遥测数据送 Gemini 2.0 Flash 做行为风险分级
- 考后自动生成 4 周补习计划并经 SMTP/webhook 派发事件报告

## 适用场景

- 在线考试中实时监考并产出告警与事件报告
- 考后为学生生成个性化补习与学习资源
- 通过仪表盘查看学生风险画像与分析图表

## 场景标签

`多智能体` `人脸识别` `语音识别` · 领域:Agent 开发

## 证据(README 行号)

> L23: **ExamIntellect** bridges this gap by introducing an autonomous **Tri-Agent AI Ecosystem**. It couples **low-latenc
> L30: - 🧠 **Multimodal LLM Behavioral Appraisal**: 30-second telemetry bundles streamed to **Google Gemini 2.0 Flash** fo
> L53: |**🛡️ Proctor Agent** `proctor_agent.py`|Real-time candidate monitoring, face presence verification, gaze deviation

## 星数曲线

```mermaid
xychart-beta
    title "RakeshBabuGajula/Exam_Intellect 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `487d3fe75938` · [字段定义](../../DATASET.md)*
