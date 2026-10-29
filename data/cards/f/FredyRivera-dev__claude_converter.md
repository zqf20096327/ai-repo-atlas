# FredyRivera-dev/claude_converter

⭐ 49 · Python · Apache-2.0 · 推送 2026-07-10 · [GitHub](https://github.com/FredyRivera-dev/claude_converter) · 个人维护

**零依赖 Python 库：把编程 agent 会话 JSONL 转为 Hugging Face messages 格式**

解析 Claude Code、Codex、Pi 三种编程 agent 的 .jsonl 会话文件（含用户提示、回复、工具调用、推理块），统一展平为 transformers tokenizer.apply_chat_template() 直接消费的 messages 列表，下游代码无需感知来源工具。提供统一 Converter 类与旧版模块级 API，含会话检查报告（记录类型统计、角色分布、token 用量）。零依赖，huggingface_hub 仅用于拉取示例非必需。限制：按文件行序线性读取，分支/多 agent 会话需自定义遍历；不提供流式加载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Claude Code / Codex / Pi 三种会话格式统一转换为 messages 列表
- 零依赖，工具调用/结果/推理块统一为 XML 风格标签
- inspect_session 输出记录类型统计、角色分布与 token 用量报告
- 附 TRL/SFTTrainer、Axolotl、LLaMA-Factory 微调数据准备示例

## 适用场景

- 把编程 agent 会话整理成微调训练数据集
- 训练前检查与过滤会话内容（剥离工具块、思考块、空轮次）
- 跨工具混合多个 agent 的会话合并为统一格式数据集

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: A zero-dependency Python module for inspecting and converting coding-agent session files (`.jsonl`) — **Claude Code*
> L12: Session JSONL (Claude Code / Codex / Pi)  →  [claude_converter]  →  messages[]  →  apply_chat_template()  →  tokens
> L152: in a format that maps directly to the `messages` list expected by every major

## 星数曲线

```mermaid
xychart-beta
    title "FredyRivera-dev/claude_converter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-29 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fcef31d1bc2b` · [字段定义](../../DATASET.md)*
