# armandcismaru/DeepTraderX

⭐ 22 · Jupyter Notebook · MIT · 推送 2026-10-26 · [GitHub](https://github.com/armandcismaru/DeepTraderX) · 个人维护

**深度学习交易代理：在多线程金融市场模拟中交易与评测**

MEng 毕业项目的深度学习交易系统：在 Dave Cliff 的 Bristol Stock Exchange 多线程扩展（TBSE）模拟交易所中，基于限价单簿 Level-2 观测数据训练神经网络交易者（DTX/DTR），可与 ZIC、ZIP、GDX、AA、Giveaway、Shaver 六种既有策略同场对比。通过配置文件、命令行或 CSV 指定交易者组合，结果输出为 CSV（含利润、最优买卖价）。本地用 pip 安装依赖运行，也提供 Docker 镜像与 AWS EKS/Kubernetes 多 Pod 并行部署方案，结果可上传 S3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 LOB Level-2 数据训练的神经网络交易代理
- TBSE 多线程模拟交易所中与 6 种经典交易策略对比
- 三种交易者组合指定方式（config/命令行/CSV 多会话）
- Docker 镜像与 AWS EKS 多 Pod 并行部署，结果上传 S3

## 适用场景

- 在模拟市场中对比深度学习交易者与传统算法策略的利润
- 批量运行多组交易者组合的市场实验并汇总结果
- 在云集群上并行执行大规模市场模拟

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L14: This repository was created as part of my final individual project for the MEng Computer Science 4th year dissertat
> L16: The results of my research indicate positive results of DeepTraderX (DTX) versus the other, well established, publi
> L40: The ```deep_trader``` directory in ```src``` contains the code used to train the Neural Network model. The trained 

## 星数曲线

```mermaid
xychart-beta
    title "armandcismaru/DeepTraderX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c3be8b3033d6` · [字段定义](../../DATASET.md)*
