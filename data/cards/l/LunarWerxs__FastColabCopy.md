# LunarWerxs/FastColabCopy

⭐ 34 · Python · MIT · 推送 2026-10-07 · [GitHub](https://github.com/LunarWerxs/FastColabCopy) · [官网](https://lunarwerx.com) · 个人维护

**给 Colab 用户的 Google Drive 多线程文件复制脚本**

Python3 脚本 fastcopy.py，通过多线程并行复制在 Google Colab 中实现两个位置（当前面向 Google Drive 到 Google Drive）之间的文件传输，作者称大量小文件场景下可达 10-50 倍速度提升。提供命令行参数控制线程数、大小限制、同步与替换等行为。使用方式为在 Colab 中通过 wget 或从 Drive 导入脚本后 import fastcopy 并以命令行运行。限制：--sync 与后续 rsync 配合会出问题；Colab 传输速度波动大，线程数仅能给建议值。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多线程并行复制 Google Drive 文件
- 命令行参数控制线程数/大小限制/同步/替换
- 通过 wget 或 Google Drive 导入脚本，在 Colab 中直接使用

## 适用场景

- 在 Colab 中快速迁移大量小文件的数据集
- 在共享 Drive 之间复制或镜像目录

## 场景标签

 · 领域:开发工具/文件传输

## 证据(README 行号)

> L8:  Python3 script to transfer files in Google Colab 10-50x faster.
> L20: FastColabCopy is a Python script for parallel (multi-threading) copying of files between two locations. Currently d

## 星数曲线

```mermaid
xychart-beta
    title "LunarWerxs/FastColabCopy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `8fb5edd3b94e` · [字段定义](../../DATASET.md)*
