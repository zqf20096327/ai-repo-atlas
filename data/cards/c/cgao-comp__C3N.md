# cgao-comp/C3N

⭐ 19 · Python · 推送 2026-02-22 · [GitHub](https://github.com/cgao-comp/C3N) · 组织维护 · 中文 README

**多模态假新闻检测论文代码：利用跨模态内容相关性**

Information Processing & Management 2025 论文的官方代码，提出利用跨模态内容相关性的多模态假新闻检测方法。基于 Python 3.7 与 PyTorch 1.8，使用 CLIP 与 Chinese-CLIP 等包；提供 Weibo 与 Twitter 两个公开数据集，部分图像裁剪文件经 Google Drive 下载。运行流程为：修改三个脚本中的保存路径，依次执行文本预处理、图像预处理脚本，再运行 main.py 训练。仓库未提供打包安装方式，需自行配置环境并准备数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 论文官方代码（IPM 2025）
- Weibo 与 Twitter 两个公开数据集
- 依赖 CLIP 与 Chinese-CLIP 做多模态处理
- 文本/图像预处理脚本加 main.py 训练流程

## 适用场景

- 复现论文中的多模态假新闻检测实验
- 在其模型基础上做假新闻检测研究
- 学习 CLIP 跨模态特征在检测任务中的用法

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L4: Jiao Qiao, Xianghua Li, Chao Gao, Lianwei Wu, Junwei Feng, Zhen Wang, Improving multimodal fake news detection by le
> L35: Run `main.py` to perform the training process.

## 星数曲线

```mermaid
xychart-beta
    title "cgao-comp/C3N 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `56953d804f98` · [字段定义](../../DATASET.md)*
