# fbgallet/roam-extension-live-ai-assistant

⭐ 62 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/fbgallet/roam-extension-live-ai-assistant) · 个人维护

**Roam Research 的 AI 助手扩展：在笔记块中直接调用 LLM**

面向 Roam Research 用户的开源扩展，把多家 LLM 接入 Roam 界面：在块内写提示词点按钮即获得插入子块的回答，或使用 Chat 面板进行对话。支持多模型切换（OpenAI、Anthropic、Gemini、Grok 等）、语音实时转录、附件输入（pdf/md/csv/docx 等）、Roam 表格 AI 自动补全、自然语言查询代理与 Ask Your Graph 图谱问答 agent。需自备各提供商 API key 按用量计费，或通过 Ollama/OpenAI 兼容服务使用免费本地模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 Roam 块与 Chat 面板中直接调用多家 LLM 并快速切换模型
- Ask Your Graph agent 用自然语言向整个图谱提问，查询代理以自然语言生成高级 Roam 查询
- 实时语音转录、多格式附件输入（.pdf/.md/.csv/.json/.docx 等）
- Roam 表格行列 AI 自动补全与 Color Highlighter 配合的内容标注工具

## 适用场景

- 在 Roam 笔记中直接向 AI 提问并把结构化回答插入块
- 用自然语言对整个 Roam 图谱做问答与查询
- 通过语音口述生成笔记内容
- 按 token 用量付费或用 Ollama 本地模型控制成本

## 场景标签

`AI 助手` `知识库管理` `语音识别` · 领域:对话与助手

## 证据(README 行号)

> L3: **AI Assistant tailor-made for Roam: the power of all the latest LLMs instantly accessible in Roam. Interact with yo
> L5: **Leverage Roam's features to write simple, structured or dynamic prompts, chat with any given part of your graph (y
> L7: **Ask your entire graph any question with Ask Your Graph agent or unlock the full power of advanced Roam queries usi

## 星数曲线

```mermaid
xychart-beta
    title "fbgallet/roam-extension-live-ai-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-27 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a3daab4eec80` · [字段定义](../../DATASET.md)*
