# microsoft/verus-copilot-vscode

⭐ 18 · Rust · MIT · 推送 2026-01-23 · [GitHub](https://github.com/microsoft/verus-copilot-vscode) · 组织维护

**VS Code 扩展：为 Rust/Verus 代码自动生成形式化证明注解**

微软维护的 VS Code 扩展，面向使用 Verus 验证 Rust 程序正确性的开发者。功能通过代码动作（灯泡按钮）触发：在选定函数内生成 Verus 证明、修复不正确的循环不变式、针对后置条件不满足或 assert 无法验证的错误生成证明；合成的证明先在 Refactor Preview 面板供用户审阅。机制上调用用户提供的 LLM 端点（当前仅支持 Azure OpenAI）与 verus 二进制，证明合成过程为非确定性。限制：仅支持无文件级依赖的单个 Rust 文件，研究性质、不建议生产/商业使用。安装需先装 Rust 与 verus-analyzer，再从 GitHub release 下载 vsix 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 代码动作生成 Verus 证明注解（函数内生成、循环不变式修复、验证错误响应）
- 证明先在 Refactor Preview 面板供用户审阅，仅修改 ghost code 不触碰可执行代码
- 调用用户提供的 Azure OpenAI 端点与 verus 二进制完成证明合成
- 可选接入 Azure AI Content Safety 防范提示攻击

## 适用场景

- 编写 Verus/Rust 代码时自动补全形式化证明注解
- 修复循环不变式或针对验证错误生成证明
- 降低 Rust 程序形式化验证的人工成本

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L76:  - Verus Copilot is a VS Code extension that can automatically generate some of the Verus proof annotations with us
> L79:  - When code action triggered, the extension will interact with user-provided OpenAI endpoints and verus binary to 

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/verus-copilot-vscode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8baa0a992404` · [字段定义](../../DATASET.md)*
