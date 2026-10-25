# osslab-pku/gfi-bot

⭐ 57 · Python · GPL-3.0 · 推送 2026-04-21 · [GitHub](https://github.com/osslab-pku/gfi-bot) · [官网](https://gfibot.osslab-pku.org) · 组织维护 · 中文 README

**给 GitHub 项目自动发现并标注 good first issue 的 ML 机器人**

面向 GitHub 开源项目维护者：自动识别并标注适合新贡献者的 good first issue，可作为 GitHub App 安装或在线注册仓库，也可自行部署。由四个模块组成：gfibot.data 周期性增量采集 issue 统计，gfibot.model 周期训练推荐模型，gfibot.backend 提供 RESTful API，frontend 为网站门户；各模块通过 MongoDB（4.2+）实例解耦读写。依赖 poetry 管理环境，需配置 GitHub access tokens，提供 Docker 镜像构建脚本。README 自述处于 pre-alpha 阶段，尚不稳定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四模块架构：数据采集、模型训练、RESTful 后端、Web 前端
- MongoDB 作为单一数据源解耦各模块
- 提供 production/ 目录下的 Docker 镜像构建脚本
- 配套 ESEC/FSE 2022 与 ICSE 2022 论文及 Zenodo 离线数据集

## 适用场景

- 开源维护者自动标注仓库中的 good first issue
- 新贡献者通过 gfibot.io 浏览推荐的首个贡献任务
- 研究者使用 Zenodo 数据集研究 GFI 推荐

## 场景标签

 · 领域:软件工程/开发工具

## 证据(README 行号)

> L9: ML-powered 🤖 for finding and labeling good first issues in your GitHub project!
> L36: 2. `gfibot.model`: Modules to periodically train GFI recommendation models based on issue statistics collected by `

## 星数曲线

```mermaid
xychart-beta
    title "osslab-pku/gfi-bot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 55 --> 58
    line [56, 57, 57]
```

2026-10-18 56 → 2026-10-25 57（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cb7d5f854407` · [字段定义](../../DATASET.md)*
