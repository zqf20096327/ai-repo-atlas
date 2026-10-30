# donaldafeith/Pytorch_Merge

⭐ 26 · Python · GPL-3.0 · 推送 2026-03-18 · [GitHub](https://github.com/donaldafeith/Pytorch_Merge) · 个人维护

**合并多个 PyTorch 模型 .bin 权重文件的命令行脚本**

提供 py_merge.py 脚本，将两个及以上 PyTorch 模型 .bin 权重文件合并为单一文件：对同名参数键取平均值，可用于合并同一模型的多分片权重，或对架构兼容的不同模型做权重平均。面向需要在本地处理模型权重文件的开发者，以 pip 包安装后通过 pytorch_merge 命令行运行，需提供 config.json、输入 bin 文件与输出路径。README 提示架构不同或训练数据不同的模型合并效果不保证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 合并多个 .bin 权重文件，同名参数取平均
- 支持多分片权重合并或不同兼容模型权重平均
- 命令行工具，指定 config/输入/输出三参数
- GPLv3+ 许可

## 适用场景

- 把多分片下载的模型权重合并为单文件
- 对架构相同的两个模型做权重平均实验
- 批量循环合并多个权重文件

## 场景标签

 · 领域:机器学习工具/模型权重处理

## 证据(README 行号)

> L11: This repository contains a script, **py_merge.py**, that can be used to merge two PyTorch model .bin files into a s
> L42: * `--bin model1.bin model2.bin model3.bin` -- All the model’s weights .bin files you want to merge. You can merge w

## 星数曲线

```mermaid
xychart-beta
    title "donaldafeith/Pytorch_Merge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6ebb78b0bc77` · [字段定义](../../DATASET.md)*
