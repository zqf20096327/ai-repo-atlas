# raghavagps/toxinpred2

⭐ 21 · Perl · GPL-3.0 · 推送 2026-05-08 · [GitHub](https://github.com/raghavagps/toxinpred2) · [官网](http://webs.iiitd.edu.in/raghava/toxinpred2) · 组织维护

**预测肽/蛋白质毒性的工具（随机森林与混合模型）**

ToxinPred2.0 用于预测、映射和扫描毒性肽：输入 FASTA 或单行简单格式序列，输出 CSV 格式的毒性判定与分数（分数与毒性潜力成正比，阈值 0-1 可调）。内置两个模型：基于氨基酸组成的随机森林模型，以及 RF+BLAST+MERCI 集成的混合模型。提供 pip 包与 Python3 独立版本；独立版需另行下载体积较大的模型文件并解压至主程序目录，混合模型依赖 BLAST 与 MERCI。由 IIIT Delhi 团队维护，配套 web 服务器。

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

- 随机森林模型（基于氨基酸组成）预测肽/蛋白毒性
- RF+BLAST+MERCI 集成的混合模型（Hybrid Score）
- 支持 FASTA 与简单格式输入，输出 CSV 结果
- 提供 pip 包（toxinpred2）与独立 Python3 版本

## 适用场景

- 我需要批量预测肽段是否具有毒性
- 在药物/蛋白治疗开发中筛选毒性候选
- 本地离线运行毒性预测而非使用 web 服务器

## 场景标签

 · 领域:生物信息学/药物发现

## 证据(README 行号)

> L2: A method for predicting toxicity of the proteins
> L69:  i) Model1 for predicting given input peptide/protein sequence as toxic and non-toxic peptide/proteins using Random

## 星数曲线

```mermaid
xychart-beta
    title "raghavagps/toxinpred2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `061a10b687fc` · [字段定义](../../DATASET.md)*
