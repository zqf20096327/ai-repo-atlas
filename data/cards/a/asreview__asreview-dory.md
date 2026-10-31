# asreview/asreview-dory

⭐ 14 · Python · MIT · 推送 2026-04-29 · [GitHub](https://github.com/asreview/asreview-dory) · [官网](https://asreview.ai) · 组织维护

**给系统综述研究者的 ASReview 扩展：提供深度学习分类与特征提取模型**

ASReview LAB 官方维护的插件，为主动学习筛选工具 ASReview 增加模型组件：7 种特征提取器（Doc2Vec、GTR T5、LaBSE、MPNet、Multilingual E5、MXBAI、XLM RoBERTa）与 5 种分类器（AdaBoost、三层神经网络、XGBoost 等）。安装后模型在 ASReview 前端与命令行可用，支持 asreview dory cache 预下载模型缓存。兼容 ASReview 2 及以上版本；macOS 使用 XGBoost 需先安装 OpenMP。

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

- 提供 7 种特征提取器（含多语 LaBSE、Multilingual E5、XLM RoBERTa）
- 提供 5 种分类器（AdaBoost、2 层/动态/热启动神经网络、XGBoost）
- asreview dory cache 命令预缓存模型避免运行时下载
- 模型可通过前端与 CLI 使用，文档与自定义模型示例在 docs/examples 目录

## 适用场景

- 系统综述筛选时使用更强 NLP 模型替代轻量模型
- 预先缓存模型以便离线或批量仿真运行
- 参考示例为自己的模型编写 ASReview 集成

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L8: ASReview Dory is an extension to the [ASReview
> L10: classification and feature extraction. The extension is maintained by the
> L54: Once installed, the plugins will be available in the front-end of ASReview, as

## 星数曲线

```mermaid
xychart-beta
    title "asreview/asreview-dory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2ece9eb04ee8` · [字段定义](../../DATASET.md)*
