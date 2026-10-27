# Intuned/selector-forge

⭐ 71 · TypeScript · MIT · 推送 2026-07-02 · [GitHub](https://github.com/Intuned/selector-forge) · [官网](https://selectorforge.ai/) · 组织维护

**浏览器扩展：选取页面元素并用 AI 生成并验证 CSS/XPath 选择器**

面向 Chrome 与 Firefox 的 MV3 浏览器扩展，供编写端到端测试、爬虫与页面自动化的开发者使用。工作流为：用户在活动页面上选取元素（单元素或从重复集合中选两个示例），扩展捕获快照并发送到 Intuned 的选择器后端，后端由 AI 提出并排序候选选择器，扩展随后对每个候选在活动 DOM 上做再验证，循环直到确定结果，仅展示通过验证的选择器。浏览器 DOM 是正确性判据，列表模式会校验完整集合以拒绝过匹配/欠匹配。构建基于 WXT 与 React。

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

- AI 提出并排序候选选择器，每个候选必须在活动 DOM 上再验证
- 支持单元素与列表（重复集合容器）两种选取模式
- 列表模式校验完整目标集合，拒绝过匹配与欠匹配的选择器
- 提供单元/真实浏览器/E2E（Playwright）三层测试

## 适用场景

- 为端到端测试生成不易失效的 CSS/XPath 选择器
- 构建爬虫时从活动页面快速获得已验证的选择器
- 对重复列表元素生成覆盖完整集合的容器选择器

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: > Pick an element on any page, get back a **reliable** selector — generated and judged by AI, then re-verified again
> L5: Selector Forge is a standalone browser extension (Chrome & Firefox, MV3) that helps you build robust CSS or XPath se
> L19: 4. The backend proposes and ranks candidate selectors; the extension **tests every candidate against the live DOM**

## 星数曲线

```mermaid
xychart-beta
    title "Intuned/selector-forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-27 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e3b74496efef` · [字段定义](../../DATASET.md)*
