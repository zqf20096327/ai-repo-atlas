# intrance7/Zeravynex

⭐ 19 · TypeScript · MIT · 推送 2026-10-14 · [GitHub](https://github.com/intrance7/Zeravynex) · 个人维护

**面向 Windows PE 文件的可解释 AI 静态恶意软件分析平台**

Zeravynex 是对 Windows PE（.exe/.dll）文件做静态恶意软件分析与威胁分诊的 Web 平台。融合确定性启发式、YARA 签名匹配、25 维特征的机器学习分类器与 SHAP 归因解释，输出样本被判为恶意的具体推手；决策融合引擎给出 0-100 风险分。仅做静态分析，不执行被上传的二进制。提供 React 18 + TypeScript 仪表盘、CLI 与 FastAPI REST 接口，后端用 Python 3.11+、前端需 Node.js 18+，从源码克隆运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PE 深度解析（头部、节权限、熵分布、时间戳）与 YARA 规则引擎
- 25 维特征机器学习分类器配 SHAP waterfall 归因解释
- 多信号决策融合引擎输出 0-100 风险分与四级判定
- CLI、FastAPI REST 接口与 React 仪表盘三种使用方式

## 适用场景

- 安全分析师上传可疑 PE 样本获取带解释的恶意判定
- 自动提取 IOC（IP、域名、URL、注册表键、互斥体）用于威胁情报
- 通过 REST API 批量集成恶意软件分诊流程

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L22: Unlike traditional black-box detection tools, Zeravynex provides **transparent, explainable security decisions** by
> L33: |🤖 **Explainable Machine Learning**|25-dimensional feature extractor with a calibrated Classifier + **SHAP waterfal

## 星数曲线

```mermaid
xychart-beta
    title "intrance7/Zeravynex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0fcc62e62ed9` · [字段定义](../../DATASET.md)*
