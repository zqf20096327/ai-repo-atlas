# bitfoundation/bitfabric

⭐ 3 · C# · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/bitfoundation/bitfabric) · [官网](https://bitfabric.co) · 组织维护

**为 .NET 开发者提供的 bit Fabric 平台、CLI 与项目模板**

本仓库包含三部分：bit Fabric 网站/应用及其服务器与 Workbench；bit CLI（nuget.org 上的 Bit.Cli），用于创建项目、在任意计算机上完成设置、生成密钥并保持更新；bit Boilerplate 项目模板（Bit.Boilerplate），是 bit new 命令的起点。其依赖的 UI 库 bit BlazorUI、bit Butil 位于 bitplatform 仓库（MIT 许可）。各部分通过 .NET SDK global.json 固定版本，构建使用 Aspire 运行服务器与 Web 应用，CI 在每个 PR 上构建测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三组件结构：Fabric 站点、Bit.Cli 工具、Bit.Boilerplate 模板
- bit CLI 支持项目创建、环境设置与密钥生成
- 依赖的 bit BlazorUI / bit Butil 等库以 MIT 许可独立发布
- GitHub workflows 对每个 PR 构建并测试

## 适用场景

- 用 bit new 从 Boilerplate 模板创建 .NET 项目
- 用 bit CLI 在新机器上初始化并维护项目
- 在 bitfabric.co 使用 Fabric 站点与应用

## 场景标签

 · 领域:软件开发工具/.NET 生态

## 证据(README 行号)

> L5:  Build with AI. Own everything.
> L14: |`src/Cli`|bit CLI: creates a project, sets it up on any computer, makes its keys and keeps it up to date|`Bit.Cli`


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `258aa98de669` · [字段定义](../../DATASET.md)*
