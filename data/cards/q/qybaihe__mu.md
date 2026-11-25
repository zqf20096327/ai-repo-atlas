# qybaihe/mu

⭐ 616 · TypeScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/qybaihe/mu) · [官网](https://usemu.dev) · 组织维护

**为编码代理提供小型判定模型的 41 类决策裁决工具**

mu 是一个编码代理工具，提供 CLI（npm 全局安装，需 Node.js 22.19+）与 macOS/Windows/Linux 桌面应用两种形态，基于 pi 构建。核心机制是把代理循环中的 41 类是/否类判定交给一个小型 judge 模型处理，覆盖输入分类、上下文取舍、工具审批与注入检测、漂移与完成判定、子代理分工五组；其中 34 个决策点默认直接执行裁决，每次裁决写入本地 ledger，支持 shadow 模式对比不同 judge。默认 judge 为 TypeSafe 托管的 Jev，可替换为本地 mude、Hugging Face 模型、自建服务器或任意 LLM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 41 个决策点交由小型 judge 模型逐题裁决，34 个默认自动执行
- 长工具输出分块准入与过期丢弃，测试日志无损折叠
- 裁决全部写入本地 ledger（mu ledger / Judge tab），支持 shadow 模式
- 提供 macOS/Windows/Linux 桌面应用与 npm CLI

## 适用场景

- 减少编码代理每步都弹出的人工审批
- 压缩代理会话中长测试日志占用的上下文
- 检测代理中途停止或未验证的完成声明
- 在换用 judge 前用 shadow 模式对比裁决效果

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L4:  Most of what a coding agent decides isn't code. It's yes/no calls, and mu hands 41 kinds of them to a small model. 
> L27: Asking the main model each of these costs tokens and its attention, and fixed rules get them wrong too often. mu as
> L29: mu comes as a command-line tool, `mu`, which does everything pi does and adds the judgment kernel, and as a desktop

## 星数曲线

```mermaid
xychart-beta
    title "qybaihe/mu 星数(近 26 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 527 --> 624
    line [535, 540, 544, 550, 552, 554, 556, 561, 563, 568, 544, 583, 591, 596, 601, 603, 604, 605, 608, 609, 610, 612, 614, 615, 616, 616]
```

2026-10-23 535 → 2026-11-25 616（+81）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `c6fe23ba702f` · [字段定义](../../DATASET.md)*
