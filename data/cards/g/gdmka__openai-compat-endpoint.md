# gdmka/openai-compat-endpoint

⭐ 10 · 推送 2026-09-18 · [GitHub](https://github.com/gdmka/openai-compat-endpoint) · 个人维护

**让 LM Studio 接入云模型的插件：本地与云推理同界面使用**

一个 LM Studio 插件（fork），在 LM Studio 的 Chat 界面中通过 Your Generators 加载后，用户可填入 API key 调用 Cerebras、Groq、OpenRouter、Claude、GPT-4o、Gemini-2.5、DeepSeek 等任何 OpenAI 兼容端点，与本地模型切换使用。新增 OpenAI/Anthropic 兼容模型的推理力度与思考支持、原生采样参数（temperature/top-p 等）的 GUI 暴露、自定义系统提示词与聊天历史全文搜索。安装通过 LM Studio Hub 的 Run in LM Studio 完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零配置接入：粘贴 API key、选模型即可在 LM Studio 内对话云模型
- GUI 内暴露原生 OpenAI 采样参数（temperature、top-p、frequency penalty 等）
- OpenAI/Anthropic 兼容模型的 reasoning effort 与 thinking 支持
- 聊天历史全文搜索与本地/云模型随时切换

## 适用场景

- 在 LM Studio 界面里同时使用本地模型与云端模型
- 用已有的各家 API key 在统一 UI 中切换多个云供应商
- 对比本地与云模型输出时保持同一聊天界面

## 场景标签

`聊天机器人` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: # OpenAI-Compatible Client for LM Studio
> L5: Turn **LM Studio** into a cloud-ready powerhouse. Access local and cloud inference simultaneously in the same app!
> L34: 2. In LM Studio → Chat → Your Generators load the plugin → hit Show Settings shortcut → pick Generators tab → paste

## 星数曲线

```mermaid
xychart-beta
    title "gdmka/openai-compat-endpoint 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `8ddc3629accc` · [字段定义](../../DATASET.md)*
