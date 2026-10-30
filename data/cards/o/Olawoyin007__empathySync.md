# Olawoyin007/empathySync

⭐ 16 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Olawoyin007/empathySync) · 个人维护

**本地优先、带克制设计的心理健康导向 AI 助手**

通过 Ollama 在本地硬件运行的 AI 对话助手，无云端调用与遥测。实用任务（写作、编程、解释）提供完整帮助；对情绪、健康、财务等敏感话题采取克制策略：简短回复、转向真人资源、不做留人的追问。安全管线含关键词分诊、LLM 分类器、回避检测与危机二次判定四层，检测到危机语言时优先引导专业/紧急资源。文档明示隐性危机语言在小模型分类器下接近漏检（1/6 vs 14B 的 6/6），并要求部署前阅读危机分诊报告。提供 Docker、install.sh 与 pip 三种安装方式，Web UI（Streamlit）与 CLI 两种运行模式，对话数据以 JSON 或 SQLite 存于本地。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四层安全管线：关键词分诊/LLM 分类器/回避检测/危机二次判定
- 敏感话题克制回复与真人资源转向，不追问留人
- 完全本地运行：Ollama 推理、无云调用、无遥测
- YAML 配置提示词与阈值，ConversationSession 类可嵌入 Python 项目

## 适用场景

- 我在本地跑一个不优化停留时长的私人 AI 助手
- 遇到情绪困扰时获得简短回应和转向真人支持的引导
- 开发者把会话安全管线嵌入自己的 Python 项目

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L24: It gives full help on practical tasks - writing, coding, explanations, and everyday taks. On sensitive topics (emot
> L26: Everything runs on your hardware via Ollama. No cloud. No external API calls. No telemetry. No engagement optimizat

## 星数曲线

```mermaid
xychart-beta
    title "Olawoyin007/empathySync 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fa057787b1fd` · [字段定义](../../DATASET.md)*
