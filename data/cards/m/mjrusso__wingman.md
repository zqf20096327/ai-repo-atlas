# mjrusso/wingman

⭐ 44 · Emacs Lisp · GPL-3.0 · 推送 2026-05-22 · [GitHub](https://github.com/mjrusso/wingman) · 个人维护

**给 Emacs 用户的 LLM 行内代码/文本补全包**

Emacs 次要模式包，提供 GitHub Copilot 风格的缓冲区内“幽灵文本”补全，是 llama.vim 插件向 Emacs 的移植。双模式：Native FIM 通过 llama.cpp 的 /infill 端点实现快速自动补全；Emulated FIM 通过 gptel 手动触发访问更多模型。异步非阻塞，带内存缓存与项目内最近文件的环形缓冲上下文。前置条件为运行中的 llama.cpp 服务端，Emulated 模式需配置 gptel；依赖 transient 与 gptel。GPL-3.0-or-later 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Native FIM 模式经 llama.cpp /infill 端点自动补全
- Emulated FIM 模式经 gptel 手动触发访问多后端模型
- 异步请求不阻塞编辑，重复请求走内存缓存
- 项目感知上下文：最近使用文件文本块环形缓冲

## 适用场景

- 在 Emacs 编程时获得自动行内补全
- 自托管 llama.cpp 保持代码不出本机地补全
- 手动切换 gptel 后端与模型获取补全

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: Wingman brings GitHub Copilot-style inline completions to Emacs, offering two powerful modes: fast, automatic comple
> L13:  - **Native FIM:** Fast, efficient completions via `llama.cpp`'s specialized `/infill` endpoint for "fill-in-the-mi
> L14:  - **Emulated FIM:** Access a broader range of models via `gptel`. These completions must always be manually trigge

## 星数曲线

```mermaid
xychart-beta
    title "mjrusso/wingman 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-28 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `76a4227e681a` · [字段定义](../../DATASET.md)*
