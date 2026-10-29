# packing-box/docker-packing-box

⭐ 68 · Python · GPL-3.0 · 推送 2026-10-03 · [GitHub](https://github.com/packing-box/docker-packing-box) · 组织维护

**打包检测研究的 Docker 工具集：打包器/检测器与数据集、ML 流水线**

面向可执行文件加壳检测研究的 Docker CLI 环境：聚合分析器、打包/脱壳工具与多种检测器，通过 YAML 配置定义条目与算法、特征，支持 PE、ELF、Mach-O 格式数据集的生成、合并、筛选与可视化，并提供基于多种算法的模型训练、测试、比较与预测工具，另支持在 algorithms.yml 中配置 LLM 分类（需挂载缓存卷）。以 docker build/run 方式安装运行，多次入选 Black Hat Arsenal Europe。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚合分析器、打包器、脱壳器与检测器，YAML 声明式配置
- 数据集生成/合并/筛选与特征可视化工具
- 多算法机器学习流水线：训练、测试、比较、预测
- 支持通过 LLM 进行打包分类（提示缓存可持久化）

## 适用场景

- 生成打包/未打包可执行文件数据集用于检测研究
- 批量打包样本并评估多种静态检测器
- 训练并比较打包检测机器学习模型

## 场景标签

`科研工具` `网络安全` · 领域:学习与行业

## 证据(README 行号)

> L10: This Docker container is a CLI environment featuring a toolkit that gathers executable analyzers, packing detectors
> L142: The *TRAIN* and *PREDICT* phases of the pipeline are achieved with the `model` tool.
> L152: LLM classification can be defined in the `LLM` section of the `algorithms.yml`. To persist prompt tuning and model

## 星数曲线

```mermaid
xychart-beta
    title "packing-box/docker-packing-box 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 66 --> 69
    line [67, 68, 68]
```

2026-10-18 67 → 2026-10-29 68（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `208d12a9fb59` · [字段定义](../../DATASET.md)*
