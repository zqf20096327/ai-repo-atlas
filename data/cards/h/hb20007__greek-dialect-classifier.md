# hb20007/greek-dialect-classifier

⭐ 10 · Jupyter Notebook · MIT · 推送 2026-02-27 · [GitHub](https://github.com/hb20007/greek-dialect-classifier) · 个人维护

**区分塞浦路斯希腊语与标准现代希腊语的文本分类器**

一个识别希腊语文本属于塞浦路斯希腊语（CG）还是标准现代希腊语（SMG）的分类器项目，附作者论文作为背景说明。仓库包含三个 Jupyter Notebook，依次覆盖语料获取（Facebook/Twitter 等来源的推文与帖子）、语料数据分析与分类器构建；`Data` 目录提供作者自行收集并按 CG/SMG 分文件标注的语料库。用户可本地克隆仓库安装依赖后运行 Notebook，或通过 Binder 在远程服务器上运行，并在 Notebook 最后一段输入自定义文本测试分类结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个 Jupyter Notebook 覆盖语料采集、数据分析与分类器构建
- 提供作者自行收集并按方言分文件标注的 CG/SMG 语料库
- 支持通过 Binder 在远程服务器直接运行，无需本地环境
- 可在 Notebook 中输入自定义文本测试分类

## 适用场景

- 判断一段希腊语文本属于塞浦路斯希腊语还是标准现代希腊语
- 复现或研究方言识别的分类器构建流程
- 获取并分析按方言标注的希腊语社交媒体语料

## 场景标签

 · 领域:自然语言处理/文本分类

## 证据(README 行号)

> L7: A classifier that identifies Greek text as either Cypriot Greek (CG) or Standard Modern Greek (SMG)
> L34: To run the code, you can clone the repository, install the dependencies, and run the Jupyter notebooks on your loca

## 星数曲线

```mermaid
xychart-beta
    title "hb20007/greek-dialect-classifier 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `4f83243be6f7` · [字段定义](../../DATASET.md)*
