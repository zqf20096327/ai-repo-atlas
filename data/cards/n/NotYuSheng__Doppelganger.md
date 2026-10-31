# NotYuSheng/Doppelganger

⭐ 15 · Python · MIT · 推送 2026-09-13 · [GitHub](https://github.com/NotYuSheng/Doppelganger) · 个人维护

**用你自己的聊天记录微调本地 LLM，模仿你写作风格的工具包**

基于 LLaMA-Factory（LoRA SFT）构建的个人数字分身训练流水线：通过平台适配器读取 Telegram/WhatsApp 聊天导出，归一化为消息流后进行会话切分、多轮合并、正则敏感数据扫描（邮箱/银行卡/IP/API key 等，可插国家标识包）与可选的 LLM 质量审计，输出 ShareGPT 格式数据集，再训练 LoRA 适配器。默认示例基座为 Qwen1.5-1.8B-Chat。训练需 CUDA GPU，摄取阶段可纯 CPU。README 自述为娱乐性实验项目而非生产工具，并要求用户自行审查数据集以符合隐私法规。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 源无关摄取：适配器解析 Telegram/WhatsApp 导出，共享会话切分/合并/扫描流水线
- 非破坏性正则敏感数据扫描 + 可选 LLM 上下文 PII 标注，输出审计报告
- ShareGPT 格式输出，loss 只掩码到自己一方的回合
- LLM 审计/脱敏默认对接本地 OpenAI 兼容服务器（vLLM/LM Studio/Ollama），数据不出本机

## 适用场景

- 把 Telegram/WhatsApp 聊天记录变成可训练的数据集并微调个人风格模型
- 训练前自动扫描聊天导出中的邮箱、卡号、API key 等敏感信息
- 用本地小模型对数据集做质量评分与 PII 标注

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L19: Doppelganger fine-tunes large language models (like Qwen) on your own chat conversations, capturing how *you* write
> L115: llamafactory-cli train configs/train_lora.yaml

## 星数曲线

```mermaid
xychart-beta
    title "NotYuSheng/Doppelganger 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `75561370ece3` · [字段定义](../../DATASET.md)*
