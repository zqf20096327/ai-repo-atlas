# noir4y/comment-translate.nvim

⭐ 20 · Lua · MIT · 推送 2026-10-11 · [GitHub](https://github.com/noir4y/comment-translate.nvim) · 个人维护

**Neovim 注释与字符串翻译插件，支持本地 LLM**

面向 Neovim 用户的翻译插件：通过悬停、沉浸式内联模式或选中替换，翻译代码注释与字符串。基于 Tree-sitter 检测目标（解析失败时回退正则），支持经典翻译 API（Google）与 LLM 后端（OpenAI/Anthropic/Gemini/Ollama），经 Ollama 本地端点可完全离线翻译，不向云端发送文本。API key 经 stdin 传给 curl，缓存仅存内存。要求 Neovim 0.10+、curl 与 plenary.nvim，经 lazy.nvim/packer.nvim 安装。

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

- 悬停翻译、沉浸式内联翻译与选中替换三种模式
- LLM 后端支持 openai/anthropic/gemini/ollama，Ollama 本地端点可完全离线
- Tree-sitter 感知的注释/字符串检测，含注入语言与多种 heredoc 场景
- API key 与请求体经 stdin 传给 curl，缓存仅内存不落盘

## 适用场景

- 在 Neovim 中悬停查看外语注释的翻译
- 沉浸式模式下批量翻译当前缓冲区的注释
- 敏感仓库中用本地 Ollama 模型做离线翻译
- 将选中字符串直接替换为译文

## 场景标签

 · 领域:开发者工具/编辑器插件

## 证据(README 行号)

> L6: Translate comments and strings directly in Neovim using hover or immersive inline views.
> L7: Supports classic translation APIs as well as LLM backends, including fully local models via Ollama.

## 星数曲线

```mermaid
xychart-beta
    title "noir4y/comment-translate.nvim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `cd663654a286` · [字段定义](../../DATASET.md)*
