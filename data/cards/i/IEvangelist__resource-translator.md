# IEvangelist/resource-translator

⭐ 71 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/IEvangelist/resource-translator) · [官网](https://ievangelist.github.io/resource-translator/) · 个人维护

**GitHub Action：为资源文件自动生成机器翻译的 PR**

一个 GitHub Action，检测仓库内本地化资源文件的变化，调用云端机器翻译服务（Azure AI Translator、AWS Translate、Google Cloud Translation 三选一，均经官方 SDK 接入）生成翻译并提交 pull request。支持 .resx/.xliff/.po/.json/.ini/.restext 六种格式。默认开启 Smart change detection：通过状态清单记录键级哈希，仅翻译新增、缺失或变更的键，保留人工编辑；snapshotOnly 模式可基于现有文件建立基线而不调用翻译服务。需按所选 provider 配置凭证，AWS 推荐 OIDC 认证。

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

- 三云翻译 provider 统一 API，各用官方 SDK 并内置重试/限流
- Smart change detection：按键级哈希仅翻译变更项，保留人工编辑
- snapshotOnly 模式从现有源/目标文件建立状态基线，避免首次全量重翻
- 支持 .resx/.xliff/.po/.json/.ini/.restext 六种资源文件格式

## 适用场景

- CI 中自动维护多语言资源文件的翻译
- 只翻译变更字符串，避免整目录重复翻译费用
- 已有部分翻译的项目建立基线后增量补翻

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L10: A GitHub Action that opens machine-translated pull requests for resource files
> L12: string changes. Choose one translation **provider** per run — **Azure AI

## 星数曲线

```mermaid
xychart-beta
    title "IEvangelist/resource-translator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-30 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0aa7d9a28484` · [字段定义](../../DATASET.md)*
