# paveldevyatov/ai-domain-name-generator

⭐ 21 · MIT · 推送 2026-10-06 · [GitHub](https://github.com/paveldevyatov/ai-domain-name-generator) · 个人维护

**把任意 AI 变成域名生成与可用性检查器的提示词/技能**

一个自包含的 PROMPT.md 提示词，可粘贴进 Claude、ChatGPT 等对话 AI，或通过 npx skills 安装为 Claude Code、Codex、Cursor 等编码代理的技能（安装后名为 find-domain）。用户用一句话描述项目，AI 按 15 种风格生成数百个候选名，再通过 DNS 与各注册局的 RDAP/whois 查询核验可用性，覆盖 1,350+ 个域名区，最终输出评分排序的前 50 个可注册域名。限制：无网络的 AI 只能生成排序不查可用性；注册局显示可注册不等于最终可购买，商标核查需人工完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件提示词，可粘贴任意 AI 或安装为编码代理技能
- 按 15 种命名风格生成数百候选并做质量预筛
- 通过注册局 RDAP/whois 核验，覆盖 1,350+ 个域名区
- 输出仅含验证可注册域名，按可读性/记忆度等项目评分排序前 50

## 适用场景

- 给新项目或产品快速头脑风暴可注册的品牌域名
- 让编码代理在开发流程中直接查询域名是否可注册
- 寻找 bit.ly 类 domain hack 域名

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: A single, self-contained prompt that turns Claude, ChatGPT, or any other capable AI into a domain name generator and
> L39: ### ✍️ Generate - hundreds of names, not ten
> L49: - 🖥️ **Coding agent with a terminal** - DNS first to drop the obviously taken names, then each zone's own registry:

## 星数曲线

```mermaid
xychart-beta
    title "paveldevyatov/ai-domain-name-generator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e2ce8380f132` · [字段定义](../../DATASET.md)*
