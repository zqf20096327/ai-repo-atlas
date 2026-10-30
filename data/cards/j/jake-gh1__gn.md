# jake-gh1/gn

⭐ 22 · Rust · Apache-2.0 · 推送 2026-07-19 · [GitHub](https://github.com/jake-gh1/gn) · 个人维护

**拉取 90 天新闻快照并用 LLM 精炼的命令行工具**

Rust 编写的命令行工具 gn：按股票代码（如 gn msft）拉取过去 90 天的新闻快照，支持本地或云端 LLM 对快照做进一步精炼，可通过 --model 参数切换模型；首次运行 gn 会编辑运行时配置，细节见 docs/config.md 与 docs/workflow.md。macOS 与 Windows 各提供一行安装脚本，代码以 Apache 2.0 许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按股票代码拉取 90 天新闻快照
- 支持本地或云端 LLM 精炼快照，--model 可切换模型
- macOS/Windows 一行脚本安装

## 适用场景

- 快速获取某只股票近 90 天的新闻汇总
- 配合本地 LLM 对新闻快照做精炼处理

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3:  gn pulls 90-day news snapshots.
> L4:  Use local or cloud LLMs to refine the snapshot.

## 星数曲线

```mermaid
xychart-beta
    title "jake-gh1/gn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `db04985c7c06` · [字段定义](../../DATASET.md)*
