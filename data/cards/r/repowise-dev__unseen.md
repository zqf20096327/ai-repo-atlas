# repowise-dev/unseen

⭐ 17 · TypeScript · MIT · 推送 2026-06-24 · [GitHub](https://github.com/repowise-dev/unseen) · 组织维护

**本地优先的实时会议助手：悬浮窗转写+AI问答+记忆库**

Electron 应用，单一 STT+LLM+存储核心提供三种界面：全局热键听写（可选用快速 LLM 清理文本后粘贴到光标处）、悬浮式会议副驾驶（Deepgram nova-3 流式转写+说话人分离，触发引擎按 YAML profile 调用 LLM 生成答案、笔记、要点），以及自动沉淀的记忆系统——每日 JSONL 日志经 LLM 蒸馏为结构化事实（分 personal/work 命名空间）并注入后续提示词。支持 Anthropic/OpenAI/Gemini/Ollama 或任意 OpenAI 兼容端点；数据默认留在本机，可选 iCloud 同步；API key 存于 OS 钥匙串。需 Deepgram key 用于转写；OCR 支持可换引擎。提供 dmg/exe/AppImage 安装包或源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Deepgram nova-3 流式转写（说话人分离）+ 触发引擎 + 悬浮 capture-invisible 答案流
- 记忆系统：每日 JSONL 日志 → LLM 蒸馏为结构化事实 → 注入提示词，分 personal/work 命名空间
- 7 个内置 YAML profile（会议纪要、问答、销售助手、讲座伴侣等），新增用例只需写一个 YAML 文件
- 本地优先：数据留本机，钥匙串加密存 key，覆盖层排除屏幕捕获，无遥测

## 适用场景

- 在会议中实时获取转写、答案与谈话要点，且不被屏幕共享捕获
- 在任何应用里用热键听写，可选 AI 清理语气词后粘贴
- 把听写、会议与笔记自动蒸馏成可被 AI 引用的个人知识库

## 场景标签

`语音识别` `知识库管理` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L23: Unseen is one STT + LLM + storage core wearing three hats:
> L40: mic → streaming STT (Deepgram nova-3, diarized)
> L43:     → your chosen LLM (streaming, prompt-cached, with your distilled memory)

## 星数曲线

```mermaid
xychart-beta
    title "repowise-dev/unseen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `519bdb649707` · [字段定义](../../DATASET.md)*
