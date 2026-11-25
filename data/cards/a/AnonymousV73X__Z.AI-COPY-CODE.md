# AnonymousV73X/Z.AI-COPY-CODE

⭐ 5 · JavaScript · 推送 2026-10-25 · [GitHub](https://github.com/AnonymousV73X/Z.AI-COPY-CODE) · 个人维护

**为 z.ai 代码块添加一键复制按钮的 Chrome/Edge 扩展**

以开发者模式加载的浏览器扩展：在 z.ai 页面的 `<pre>` 代码块与 CodeMirror 编辑器上注入悬停显示的 Copy 按钮，通过 MutationObserver 捕获动态加载内容，点击后经 CodeMirror state API（或 textContent 兜底）读取文本并写入剪贴板。仅声明 clipboardWrite 与 z.ai host 两项权限，README 声明无网络请求与遥测，全部在页面本地运行。仅提供开发者模式安装方式，无应用商店发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 pre 块与 CodeMirror 编辑器上注入一键复制按钮
- MutationObserver 处理动态加载的代码块
- 仅 clipboardWrite 与 z.ai host 权限，无外部请求
- 复制后按钮显示绿色 Copied! 反馈 2 秒

## 适用场景

- 从 z.ai 对话回复中快速复制生成的代码
- 避免手动框选长代码片段
- 在 Edge/Chrome 上以开发者模式加载使用

## 场景标签

 · 领域:浏览器扩展/开发效率工具

## 证据(README 行号)

> L3: > A lightweight Chrome / Edge browser extension that adds a **Copy** button to every code block and CodeMirror edito
> L9: - 🔒 **Privacy first** — zero network requests, zero telemetry, zero external dependencies
> L43: 1. Scans the page for `.cm-editor` elements (CodeMirror) and `<pre>` code blocks

## 星数曲线

```mermaid
xychart-beta
    title "AnonymousV73X/Z.AI-COPY-CODE 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-16", "2026-11-25"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-11-08 4 → 2026-11-25 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `080a722b5a0f` · [字段定义](../../DATASET.md)*
