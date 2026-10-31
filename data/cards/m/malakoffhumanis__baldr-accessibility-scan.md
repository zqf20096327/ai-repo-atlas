# malakoffhumanis/baldr-accessibility-scan

⭐ 16 · TypeScript · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/malakoffhumanis/baldr-accessibility-scan) · 组织维护

**给开发与合规团队的 RGAA/WCAG 网页无障碍自动审计工具**

开源 Node.js 工具（npm 包），用 Puppeteer 驱动 headless 浏览器遍历站点、运行 axe-core 检查，评估 RGAA 与 WCAG 合规性并输出 HTML/JSON/CSV 报告、合规评分与修复建议。支持多页面用户旅程、需认证区域、cookie 横幅处理与 CI/CD 集成；同一包提供 CLI（baldr）与带 API key 保护的 HTTP API 服务器（baldrd）。AI 为可选增强：LLM（默认 OpenAI 兼容端点、gpt-4o）用于自然语言定位元素、自由指令步骤与深度分析，static 模式无需任何 AI 即可运行。面向无障碍专家、前端开发、QA、公共机构等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- axe-core + Puppeteer 自动化审计，输出 HTML/JSON/CSV 报告与合规评分
- 支持多页面旅程、站点认证（登录+密码）与 cookie 横幅自动接受
- 同一 npm 包提供 CLI 与 HTTP API（X-API-Key、Prometheus /metrics）两种模式
- LLM（OpenAI 兼容端点）为可选增强：自然语言定位元素、ai 指令步骤、full/intel 分析模式

## 适用场景

- 开发阶段持续做无障碍自动审计并入 CI/CD 流水线
- 上线前验证站点对 RGAA/WCAG 参照的合规情况
- 审计需登录的认证区域与动态交互页面

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L17: **Contrairement aux scanners d'accessibilité traditionnels, BALDR analyse des parcours utilisateurs complets, y com
> L135: BALDR reçoit une **requête d'audit** (CLI ou API), pilote un navigateur headless
> L239: |`static`|axe-core seul, sans IA — le plus rapide.|

## 星数曲线

```mermaid
xychart-beta
    title "malakoffhumanis/baldr-accessibility-scan 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c99881ad8a1a` · [字段定义](../../DATASET.md)*
