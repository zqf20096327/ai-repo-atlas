# DK-Jang/MOCHA_SIGASIA2023

⭐ 25 · Python · NOASSERTION · 推送 2026-05-05 · [GitHub](https://github.com/DK-Jang/MOCHA_SIGASIA2023) · [官网](https://dk-jang.github.io/MOCHA_SIGASIA2023/) · 个人维护

**SIGGRAPH Asia 2023 论文 MOCHA 官方实现：实时动作特征化**

论文《MOCHA: Real-Time Motion Characterization via Context Matching》的官方代码库，提供数据准备脚本、预训练模型与 demo：运行 test_fullframework.py 对输入 bvh 动作做 motion characterization，生成 Src_*.bvh（真实源动作）与 Ours_*.bvh（特征化输出）。安装采用 git clone 源码加 conda 环境，数据与预训练网络通过 download.sh 获取。训练代码尚未发布（清单中为未勾选项）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供预训练模型与 demo，生成 bvh 格式特征化动作
- 数据准备脚本可从原始 bvh 生成镜像训练数据
- conda 环境一键安装依赖

## 适用场景

- 运行论文 demo 复现 motion characterization 结果
- 基于预训练模型生成风格化动作数据
- 查看论文方法实现用于研究参考

## 场景标签

 · 领域:计算机图形学/动作合成

## 证据(README 行号)

> L1: # MOCHA: Real-Time Motion Characterization via Context Matching
> L41: To generate motion characterization results, run following commands:

## 星数曲线

```mermaid
xychart-beta
    title "DK-Jang/MOCHA_SIGASIA2023 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `17ee081e1cbc` · [字段定义](../../DATASET.md)*
