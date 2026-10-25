# SuperJJ007/papermachine

⭐ 66 · TypeScript · MIT · 推送 2026-09-12 · [GitHub](https://github.com/SuperJJ007/papermachine) · 个人维护 · 中文 README

**展示分析全过程的 AI 数据分析桌面应用：本地跑 Python 和 R**

面向研究人员、商业分析师与数据分析师的桌面应用（macOS/Windows）：用一句话提出需求，由 AI 在本机 Python/R 内核上执行数据清洗、建模与绘图。核心机制是过程可审计——agent trace 展示每步运行的代码与输出，图表等产物可回溯到生成它的代码、日志与运行环境，数据与变量改动开放查看。模型调用走 DeepSeek API（需自备 key），本地自带 22 包科学计算环境（约 6GB 磁盘）。Windows 版为 experimental/beta，沙箱仅文件写限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent trace：每步运行的代码、输出与内核状态可查看
- 图表/表格产物可回溯到代码、日志、提问与环境四个来源
- 自带 micromamba 与 22 包 Python/R 科学环境，不依赖用户已有 conda
- 图表可直接在面板编辑并保留 v1/v2 双版本（人类编辑有标记）

## 适用场景

- 用一句话让 AI 在本地完成数据清洗、统计建模与出图
- 向审阅者展示每个图表背后的代码与执行过程
- 对 AI 分析结果做人工修正并保留修改前后版本

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L11: PaperMachine is a desktop app for everyone whose work runs on data — researchers, business analysts, data analysts.
> L95: The window talks to a local host process on your own machine. The host owns one Python kernel and one R kernel per 

## 星数曲线

```mermaid
xychart-beta
    title "SuperJJ007/papermachine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-25 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `abafafd1d06d` · [字段定义](../../DATASET.md)*
