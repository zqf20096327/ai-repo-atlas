# feyninc/pulpie

⭐ 80 · HTML · Apache-2.0 · 推送 2026-07-01 · [GitHub](https://github.com/feyninc/pulpie) · [官网](https://usefeyn.com/blog/pulpie-pareto-optimal-models-for-cleaning-the-web/) · 组织维护

**编码器模型从 HTML 中抽取正文内容并输出 HTML/Markdown**

Python 库，内置基于 EuroBERT 的三个编码器模型（210M/610M/2.1B，共享分词器），以单次前向传播对页面每个内容块做内容/样板二分类，剥离导航、广告、侧栏与页脚后重建输出，可选转换为 Markdown。四阶段流水线：简化、分块（最长 8,192 token）、分类、重建；批量场景提供 Pipeline 在 CPU 预处理与 GPU 推理间重叠并可跨多 GPU 负载均衡。模型首次使用时从 Hugging Face 下载，支持指定本地 checkpoint 与强制 CPU 运行。面向需要大规模网页正文清洗的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单次编码器前向传播完成整页块级分类，L4 上 13.7 页/秒
- 三个 EuroBERT 系模型（Small/Base/Large），Small 为默认推荐
- Pipeline 支持 CPU/GPU 重叠与多 GPU 批量抽取
- 可选 markdown extra 输出 Markdown

## 适用场景

- 大规模清洗网页、构建 RAG 语料时剥离样板内容
- 批量将 HTML 正文转为 Markdown
- 在受限 GPU（如 L4）上以低成本跑网页抽取

## 场景标签

`网页抓取` `文档解析` · 领域:效率与自动化

## 证据(README 行号)

> L19: Pulpie extracts the main content from raw HTML, stripping navigation, ads, sidebars, and footers. It uses small enc
> L98: 3. **Classify.** A single encoder forward pass labels every block as content or boilerplate.

## 星数曲线

```mermaid
xychart-beta
    title "feyninc/pulpie 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 79 --> 81
    line [80, 80]
```

2026-10-18 80 → 2026-10-29 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f8b0293d44c4` · [字段定义](../../DATASET.md)*
