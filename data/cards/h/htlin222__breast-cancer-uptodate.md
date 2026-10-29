# htlin222/breast-cancer-uptodate

⭐ 20 · Python · 推送 2026-04-19 · [GitHub](https://github.com/htlin222/breast-cancer-uptodate) · 个人维护 · 中文 README

**自动生成肿瘤科每周治疗趋势繁体中文周报的工具**

面向肿瘤领域研究者的自动化周报生成器：从 OpenEvidence AI、OncDaily RSS、OncLive、ESMO、ClinicalTrials.gov 等来源爬取乳腺癌治疗动态，按关键词与药物分组过滤，生成 reports/YYYY-Wxx.md 格式的繁体中文周报，push 到 main 后由 GitHub Actions 自动发布至 Wiki。系统设计为 cancer-agnostic：切换癌种只需修改 source/ 下五个 YAML 配置（关键词、药物分组、搜索字串、来源、种子账号），无需改 Python 代码。默认配置为乳癌，示例演示切换到 DLBCL 淋巴瘤。

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

- 聚合 OpenEvidence AI、OncDaily、OncLive、ESMO、ClinicalTrials.gov 五类来源
- cancer-agnostic 设计：改 5 个 YAML 文件即可切换癌种，不动 Python 代码
- GitHub Actions 自动发布周报到 Wiki 并重建索引
- 基于 uv 的 Python 安装与运行流程

## 适用场景

- 跟踪乳腺癌每周治疗趋势与临床试验动态
- 切换配置后跟踪淋巴瘤等血液肿瘤的治疗进展
- 以 Wiki 形式向团队自动发布肿瘤治疗周报

## 场景标签

`网页抓取` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L3: 自動生成腫瘤科每週治療趨勢報告，以繁體中文撰寫（英文醫學名詞不翻譯）。
> L7: 資料來源：OpenEvidence AI · OncDaily RSS · OncLive · ESMO · ClinicalTrials.gov

## 星数曲线

```mermaid
xychart-beta
    title "htlin222/breast-cancer-uptodate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `d8c7ffff4596` · [字段定义](../../DATASET.md)*
