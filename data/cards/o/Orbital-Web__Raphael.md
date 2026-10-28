# Orbital-Web/Raphael

⭐ 25 · C++ · AGPL-3.0 · 推送 2026-07-26 · [GitHub](https://github.com/Orbital-Web/Raphael) · 个人维护

**超人类水平 UCI 国际象棋引擎（NNUE），附带图形界面**

C++ 编写的 UCI 国际象棋引擎，使用自研 NNUE 评估（自生成训练数据）与手工评估（HCE），搜索部分实现 alpha-beta 剪枝、迭代加深、置换表、多种剪枝/ reductions/ extensions、Lazy SMP 多线程与 NUMA 线程绑定等；另附基于 SFML 的 GUI，可人机对弈或引擎对局。提供 Windows 与 Linux/WSL 预编译二进制，也可用 Make/g++ 从源码构建。面向棋类爱好者和 UCI 软件用户，CCRL Blitz 达 3700+ 等级分。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自研 NNUE 评估（自生成训练数据，多层网络、Finny tables 等）
- UCI 兼容，可接入其他 UCI 软件
- Lazy SMP 多线程与 NUMA 线程绑定
- SFML 图形界面支持人机对弈与引擎对局

## 适用场景

- 在国际象棋 GUI 软件中作为分析或对弈引擎
- 通过自带 SFML 界面直接对弈或观看引擎对局
- 研究引擎搜索与 NNUE 训练技术（附 NNUE 历史文档）

## 场景标签

 · 领域:游戏/博弈引擎

## 证据(README 行号)

> L3: Raphael is a superhuman UCI Chess Engine built using C++.
> L220:  - [x] NNUE (`v2.0+`)
> L261: All iterations of Raphael's NNUE were trained on self-generated training data.

## 星数曲线

```mermaid
xychart-beta
    title "Orbital-Web/Raphael 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `91000f2d2e59` · [字段定义](../../DATASET.md)*
