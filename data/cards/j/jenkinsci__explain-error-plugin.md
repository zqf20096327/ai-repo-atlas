# jenkinsci/explain-error-plugin

⭐ 46 · Java · MIT · 推送 2026-10-24 · [GitHub](https://github.com/jenkinsci/explain-error-plugin) · [官网](https://plugins.jenkins.io/explain-error/) · 组织维护

**Jenkins 插件：用 AI 解释失败构建的原因并给出修复建议**

面向 Jenkins 用户的构建失败解释插件：读取失败步骤的日志（默认最多 200 行，可按正则过滤），调用用户选择的 AI 生成根因标题、摘要、修复步骤与失败行定位，展示在控制台页、Stages 页与构建侧边栏，并可通过 REST API 获取。支持 12 种 AI 提供商（含私有端点与自托管模型），可自动解释所有失败构建（默认每小时 30 次上限），带请求配额与用量指标。实验性 AI auto-fix 会提交新分支并开 PR，从不自动合并。要求 Jenkins 2.528.3 及以上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 12 种 AI 提供商，含私有端点、公司网关与自托管模型
- explainError() Pipeline 步骤可返回结构化字段用于通知与路由
- 自动解释所有失败构建，带每小时/并发限额与重复失败复用机制
- 实验性 AI auto-fix：生成修复 PR，人工审查，从不自动合并

## 适用场景

- 构建失败后快速定位根因，不用逐行翻控制台日志
- 流水线中自动调用解释步骤并发送通知
- 各团队通过文件夹配置使用各自的语言、指令与提供商

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: Explain Error turns a failed Jenkins build into a short explanation: what broke, why, and how to fix it. It reads th
> L8: log of the step that failed, asks the AI provider you choose, and shows the answer on the build, so nobody has to di
> L22: - **Twelve AI providers**: Anthropic (Claude), AWS Bedrock, Azure OpenAI, Custom Okta AI, DeepSeek, Google Gemini,

## 星数曲线

```mermaid
xychart-beta
    title "jenkinsci/explain-error-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-26 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9a3b1e054281` · [字段定义](../../DATASET.md)*
