# personizeai/governed-memory

⭐ 49 · MIT · 推送 2026-03-18 · [GitHub](https://github.com/personizeai/governed-memory) · [官网](https://personize.ai/white-paper) · 组织维护

**论文《Governed Memory》的合成数据集与实验协议（E01–E15）**

配套论文 'Governed Memory: A Shared Layer for Accuracy and Compliance Across Agentic Workflows' 的实验资源库：提供全合成业务内容数据集（会议转写、邮件、聊天、文档、通话笔记等，均带 ground truth 旁车文件）、E01–E15 共 15 个实验的可复现协议、属性抽取 schema 集合与 API 端点文档。复现需接入 Governed Memory API（付费 workspace 的 API key），通过 npm 安装 @personize/sdk 调用 memorize/smartRecall/evaluate 等端点。数据集含 250 条标注样本、多源实体、冲突对与对抗治理场景；引用待论文发表后补充。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 个实验协议，结果均已包含
- 250 条带 ground truth 的标注内容样本（5 类内容类型）
- 30 对新旧冲突对与 50 个对抗治理场景
- 三个可导入的属性抽取 schema 集合

## 适用场景

- 复现论文中的治理记忆实验结果
- 客观评测抽取召回与治理路由精度
- 按同方法生成更多合成测试样本

## 场景标签

`Agent 记忆` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: Synthetic datasets and experiment protocols for the paper **"Governed Memory: A Shared Layer for Accuracy and Compli
> L11: 1. **Synthetic datasets** — business content generated specifically to stress-test governed memory capabilities, ea
> L12: 2. **Experiment protocols** — reproducible measurement procedures for each capability claim in the paper

## 星数曲线

```mermaid
xychart-beta
    title "personizeai/governed-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-30 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5b854ca2603c` · [字段定义](../../DATASET.md)*
