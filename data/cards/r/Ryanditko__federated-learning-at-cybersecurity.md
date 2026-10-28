# Ryanditko/federated-learning-at-cybersecurity

⭐ 31 · Python · 推送 2026-05-04 · [GitHub](https://github.com/Ryanditko/federated-learning-at-cybersecurity) · 组织维护

**科研项目：检测并缓解联邦学习中的投毒攻击**

本科科研启动项目（Iniciação Científica，2024-2026，Faculdade Impacta），研究联邦学习系统中投毒攻击的检测与缓解。实现中心化服务器加多客户端的联邦训练模拟、多种攻击（Sign Flipping、梯度操纵、模型投毒、拜占庭），并以五种离群点检测技术（Isolation Forest、LOF、One-Class SVM、Elliptic Envelope、DBSCAN）识别恶意客户端并做鲁棒聚合。在 Iris、Bank Marketing、NSL-KDD 等数据集上实验，以准确率/F1/AUC-ROC 等指标量化攻击影响。README 未给出安装运行命令，项目仍在进行中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 模拟中心服务器+多客户端的联邦学习架构与投毒攻击管道
- 实现并比较 5 种离群点检测技术识别恶意客户端
- 在 Bank Marketing、Iris、NSL-KDD 等数据集上量化攻击影响
- 定义了从更新收集、特征提取、离群过滤到鲁棒聚合的防御流水线

## 适用场景

- 研究联邦学习投毒攻击对模型性能的影响
- 比较不同离群点检测方法在恶意客户端识别上的表现
- 为分布式 ML 系统的防御方案设计提供实验参考

## 场景标签

`科研工具` `网络安全` · 领域:学习与行业

## 证据(README 行号)

> L18: Este projeto de Iniciação Científica investiga estratégias de **detecção e mitigação de ataques por envenenamento**
> L22: Este estudo combina **revisão integrativa da literatura** com **implementações práticas** e **simulações computacio
> L308: **Tipo**: Iniciação Científica

## 星数曲线

```mermaid
xychart-beta
    title "Ryanditko/federated-learning-at-cybersecurity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a2e6594a2f7e` · [字段定义](../../DATASET.md)*
