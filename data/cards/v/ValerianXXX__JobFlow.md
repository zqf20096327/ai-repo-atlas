# ValerianXXX/JobFlow

⭐ 197 · Python · MIT · 推送 2026-09-06 · [GitHub](https://github.com/ValerianXXX/JobFlow) · 个人维护

**本地优先的 Windows 求职申请工作流：AI 生成有据材料，人工确认提交**

面向 Windows 用户的求职申请桌面工作流：导入简历后由本地/回环模型重构经历实体并生成需证据支撑的 Claim 候选，构建 Candidate Profile 与 Answer Bank；从官方招聘页验证职位与 ATS 路由，生成可审查的申请包，在用户在场时填充已批准字段，并在最终提交前停下交由用户手动点击。敏感数据经 Windows DPAPI 加密，后台仅限最长七天的只读职位发现。当前为 Alpha，v0.7.0 签名稳定版尚未发布，存在浏览器扩展版本不匹配问题。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Claim 候选需来源证据与申请人批准后才可外部使用
- 最终提交永久保留为用户手动操作，登录/验证码/MFA 一律停下
- 复用 Hermes/OpenClaw/Ollama/LM Studio/LocalAI/llama.cpp/vLLM 等既有模型连接且不复制凭据
- 私有数据经 Windows DPAPI 加密，数据与应用目录分离

## 适用场景

- 在本地整理简历事实并生成有据可查的申请材料
- 从官方招聘页出发，经审查门控半自动填写 ATS 申请表
- 按批准的公开来源订阅最多七天的候选职位到本地收件箱

## 场景标签

`工作流自动化` `AI 写作` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: JobFlow is a local-first, AI-centered job application workflow for Windows. It turns a resume, approved applicant fa
> L17: 3. Uses AI to reconstruct experience entities, preserve metrics, and produce source-grounded Claim candidates.
> L51: An AI connection is accepted only after a structured capability test. Agent requests use an isolated, zero-tool cha

## 星数曲线

```mermaid
xychart-beta
    title "ValerianXXX/JobFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 198 --> 200
    line [199, 199]
```

2026-10-18 199 → 2026-10-22 199（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `94a6da7bbfe9` · [字段定义](../../DATASET.md)*
