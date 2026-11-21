# pabroux/llm-engineers-handbook

⭐ 10 · Python · MIT · 推送 2026-08-13 · [GitHub](https://github.com/pabroux/llm-engineers-handbook) · [官网](https://www.amazon.com/LLM-Engineers-Handbook-engineering-production/dp/1836200072/) · 个人维护

**LLM Engineer's Handbook 一书官方仓库的 Pixi 移植版**

这是 Paul Iusztin 与 Maxime Labonne 所著《LLM Engineer's Handbook》官方仓库的适配版本，唯一改动是用 Pixi 替换原书的 Poetry 及其 Poe the Poet 插件。仓库只修改 pyproject.toml 与 pixi.lock 两个文件，通过 pixi.lock 锁定包版本保证可复现性；读者可用 pixi install 安装依赖，并将书中的 poe 命令替换为 pixi run 执行。另含 dev（QA）与 aws 两个附加环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用 Pixi 替换 Poetry 与 Poe the Poet 的适配版
- pixi.lock 锁定包版本保证可复现性
- 提供 dev 与 aws 附加环境，可用 -e 选项切换
- 可与官方仓库配合使用（复制两个文件即可）

## 适用场景

- 按《LLM Engineer's Handbook》一书学习时用 Pixi 管理环境
- 在已有官方仓库克隆上复制两个文件改用 Pixi
- 运行书中示例的本地基础设施与 QA/AWS 任务

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: This is a Pixi-based adaptation of the official repository LLM Engineer's Handbook by Paul Iusztin and Maxime Labonn
> L28: Replace any call or task made in the book with `poe` by `pixi run`:

## 星数曲线

```mermaid
xychart-beta
    title "pabroux/llm-engineers-handbook 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-21"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-19 10 → 2026-11-21 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `5d8b5d26b42e` · [字段定义](../../DATASET.md)*
