# alexandriashai/cbrowser

⭐ 18 · TypeScript · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/alexandriashai/cbrowser) · [官网](https://cbrowser.ai) · 组织维护

**带认知模拟的浏览器自动化测试工具：预测用户在何处放弃**

基于 Node.js/TypeScript 的浏览器自动化工具，提供 CLI、库与 130+7 工具的 MCP 服务器。核心机制包括：八层序贯认知传输链（视觉复杂度、认知负荷、Hick-Hyman 决策、运动、可读性等）按 persona 评分并预测流失；21 个内置 persona（含 11 个无障碍 persona）；注意力热图叠加与 AI 友好度审计（agent-ready、llms.txt 生成等）。基础导航/截图/测试命令免费无需 API key，认知 journey 类功能需 Anthropic API key（每步一次模型调用）。20.0 为破坏性版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 八层序贯认知传输链按 persona 计算认知成本与流失风险
- 21 个内置 persona（10 通用 + 11 无障碍），支持自定义
- 130+7 个 MCP 工具，含认知评分、注意力热图、AI 友好度审计
- 基础命令免费无需 key；认知 journey 类功能需 Anthropic API key

## 适用场景

- 测试网站在不同用户 persona 下的认知负担与流失风险
- 审计站点对 AI agent 与屏幕阅读器的可感知性
- 生成注意力热图与 CTA 捕获率分析
- 为站点生成 AI 可读的 llms.txt

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: > **Browser automation that thinks like your users.** 130 MCP tools, 21 built-in personas, a CLI, and a library. It 
> L37: |Free, no key|Needs an Anthropic API key (each step is a model call)|
> L39: |`navigate`, `click`, `fill`, `type`, `scroll`, `screenshot`, `extract`, `evaluate`|`cognitive-journey`|

## 星数曲线

```mermaid
xychart-beta
    title "alexandriashai/cbrowser 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [19, 18, 18]
```

2026-10-18 19 → 2026-10-30 18（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `d5d764546656` · [字段定义](../../DATASET.md)*
