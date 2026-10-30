# damianofalcioni/pi-for-word

⭐ 16 · JavaScript · MIT · 推送 2026-05-06 · [GitHub](https://github.com/damianofalcioni/pi-for-word) · [官网](https://damianofalcioni.github.io/pi-for-word/) · 个人维护

**在 Word 中嵌入 Pi Agent 助手的 M365 任务窗格插件**

Pi4Word 是一个 Microsoft Word 任务窗格加载项，通过 @mariozechner/pi-agent-core 嵌入 Pi Agent 驱动的 AI 助手，供 Word 用户在文档内使用。提供生产与本地开发两份 manifest：生产版指向 GitHub Pages 托管构建，可通过 Word 网页版上传或 Windows 受信任目录加载；本地开发需 Node.js/npm、桌面版 Word 与 localhost HTTPS，通过 npm 脚本构建与旁加载。构建流程包含测试、lint 与 esbuild 打包，输出至 public/ 目录。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Word 任务窗格加载项，嵌入基于 pi-agent-core 的 AI 助手
- 提供生产（GitHub Pages 托管）与本地开发两份 manifest
- npm 脚本覆盖证书生成、HTTPS 服务、Word 旁加载与构建

## 适用场景

- 在 Word 文档处理流程中直接调用 Pi Agent 助手
- 以加载项形式在 Word 网页版或 Windows 桌面版使用
- 本地开发并旁加载调试自定义构建

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: **Pi4Word** is a Microsoft Word task pane add-in that embeds a Pi Agent-powered assistant using `@mariozechner/pi-ag
> L13: |`manifest.production.xml`|Production usage in Word|`https://damianofalcioni.github.io/pi-for-word/public/index.htm

## 星数曲线

```mermaid
xychart-beta
    title "damianofalcioni/pi-for-word 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8f2b0c468844` · [字段定义](../../DATASET.md)*
