# dorukozerr/kisuke.vim

⭐ 18 · Vim Script · MIT · 推送 2026-08-24 · [GitHub](https://github.com/dorukozerr/kisuke.vim) · 个人维护

**在 Vim 分屏内进行 LLM 对话的极简聊天插件**

Vim 插件，将 LLM 聊天以分屏 buffer 形式嵌入编辑器：支持多会话管理（创建/切换/删除/恢复）、本地会话持久化、文件上下文标记与可视模式代码块选取作为上下文。提供商覆盖 Anthropic、OpenAI、Google、Grok，Anthropic 模型另支持 Web 搜索。首次使用时提示输入 API key，配置存于 ~/.config/kisuke/config.json。范围限定于聊天/会话/上下文，不含行内补全与多步 agent 流程；构建需全局安装 bun。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多提供商支持：Anthropic、OpenAI、Google、Grok 及各自模型列表
- 多会话管理与本地会话持久化
- 文件与代码块的上下文标记机制
- Anthropic 模型支持 Web 搜索

## 适用场景

- 在 Vim 内直接与 LLM 对话，无需离开编辑器
- 将当前文件或选中的代码块作为提示上下文
- 维护多个聊天会话并随时恢复

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L9: Kisuke.vim is a Vim plugin that brings LLM chat into the editor as a split buffer, with multi-provider support, loca
> L22: - Multiple providers and models (Anthropic, OpenAI, Google, Grok)

## 星数曲线

```mermaid
xychart-beta
    title "dorukozerr/kisuke.vim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `0313b835d41f` · [字段定义](../../DATASET.md)*
