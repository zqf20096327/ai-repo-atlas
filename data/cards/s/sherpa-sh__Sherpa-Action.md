# sherpa-sh/Sherpa-Action

⭐ 22 · Apache-2.0 · 推送 2026-01-26 · [GitHub](https://github.com/sherpa-sh/Sherpa-Action) · [官网](https://www.sherpa.sh) · 组织维护

**用自然语言驱动 AI 完成多云部署的 Claude Code 插件/GitHub Action**

以 Claude Code 插件形式提供的部署工具：用户用自然语言描述部署需求（框架、云商、域名、CDN、负载均衡等），Sherpa 调用 Claude Code 执行 /Sherpa/deploy 命令自动创建与配置基础设施。通过 GitHub Action 集成到仓库工作流，也可本地以 claude --plugin-dir 方式运行。将项目理解以 memories 文件（.sherpa.sh/）形式提交回仓库以维持部署间上下文。当前支持 Cloudflare 与 AWS 及 Next.js 框架，多数云商与框架在路线图中标记为 Planned；需 Anthropic API key 与各云商凭证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言 prompt 生成部署配置，无需手写 Terraform
- 以 GitHub Action 形式运行，或作为 Claude Code 插件本地使用
- memories 机制（.sherpa.sh/）记录已配置资源与构建命令，加速后续部署
- 静态站点、Serverless 函数、EC2 供给、SSL 证书当前标记为 Supported

## 适用场景

- 推送代码后用自然语言 prompt 自动部署到 Cloudflare 或 AWS
- 在 Claude Code CLI 中以对话方式测试部署流程
- 为自托管服务器获得类似 Vercel/Netlify 的推送即部署体验

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L123: 1. Runs Claude Code with the Sherpa plugin
> L124: 2. Executes the `/Sherpa/deploy` command with your prompt (See command descriptions below)

## 星数曲线

```mermaid
xychart-beta
    title "sherpa-sh/Sherpa-Action 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5d22fc5d59e5` · [字段定义](../../DATASET.md)*
