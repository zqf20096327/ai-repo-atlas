# matheusmaldaner/PlatosCave

⭐ 17 · Python · NOASSERTION · 推送 2026-05-19 · [GitHub](https://github.com/matheusmaldaner/PlatosCave) · 个人维护

**用多智能体验证研究论文完整性的系统**

面向科研人员的论文可信度分析系统：接受 PDF 上传或 URL，抽取全文并用 LLM 分解为原子声明，构建带角色标签（Hypothesis/Evidence/Method/Conclusion）的有向无环图；随后派发基于浏览器的智能体对照外部来源独立验证各声明，按可信度、相关性、证据强度、方法严谨性、可复现性、引用支持六个维度打分，经信任门控传播得出论文级完整性分数。前端为 Gatsby.js+React，后端 Python，浏览器自动化以 Docker 部署，需 Browser-Use 与 Exa API key；许可证限于研究与学术用途，提供在线部署与本地运行两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 将论文分解为原子声明并构建角色感知 DAG
- 浏览器智能体对照外部来源独立验证各节点
- 六维度评分与信任门控传播得出论文完整性分数
- 前端交互式图谱展示验证结果

## 适用场景

- 上传论文 PDF 快速核查其声明的外部依据
- 审稿或文献综述时评估论文可信度
- 通过可视化图谱理解论文论证结构

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L26: 2. **Decompose** -- breaks the paper into atomic claims using an LLM
> L29: 5. **Compile Evidence** -- aggregates agent findings, scoring each node on six dimensions (credibility, relevance, 

## 星数曲线

```mermaid
xychart-beta
    title "matheusmaldaner/PlatosCave 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `15dae2b69f81` · [字段定义](../../DATASET.md)*
