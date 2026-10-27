# DvorakDwarf/Witness-of-Babel

⭐ 28 · Python · GPL-3.0 · 推送 2026-03-15 · [GitHub](https://github.com/DvorakDwarf/Witness-of-Babel) · 个人维护

**在随机噪声图像中筛选“有意义图像”的 CNN 概念项目**

基于 PyTorch 的浅层 CNN，在 24x24 灰度随机张量（受限版 Canvas of Babel）中高速扫描（作者机器约 45 万张/秒），按阈值上报模型认为“看起来有内容”的图像；模型以 tiny-imagenet 训练，仓库附带预训练模型与自定义训练入口。提供普通搜索脚本和带 Discord 通知的机器人两种运行方式，结果写入日志或推送到 Discord 频道。作者声明这不是可行的图像生成方案，属概念性实验项目。需 Python 环境与 tiny-imagenet 数据集，GPU 可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CNN 对随机噪声图像按阈值筛选并上报候选图像
- 附带预训练模型，也可用 main.py 自行训练
- 支持 Discord 机器人推送发现的图像
- 受限 Canvas：24x24 灰度，约 10^1728 张可能图像

## 适用场景

- 作为概念实验运行，在随机噪声中寻找“像图像”的输出
- 通过 Discord 通知接收筛选结果
- 改造或扩展该项目探索类似想法

## 场景标签

 · 领域:概念性 AI 实验/图像分类

## 证据(README 行号)

> L3: AKA the art critic of Babel if you are feeling funny. This is an AI made for the sole purpose of sifting through ran
> L30: The AI was trained on tiny-imagenet and the architecture is a painfully shallow CNN. The "Canvas" is a random tenso

## 星数曲线

```mermaid
xychart-beta
    title "DvorakDwarf/Witness-of-Babel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-27 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `caa79fde6f25` · [字段定义](../../DATASET.md)*
