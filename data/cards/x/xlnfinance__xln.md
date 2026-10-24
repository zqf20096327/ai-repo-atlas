# xlnfinance/xln

⭐ 102 · TypeScript · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/xlnfinance/xln) · [官网](https://xln.finance) · 个人维护

**信用+抵押双边账户的 L2 网络：让金融账户状态可验证**

面向 EVM 及未来 CBDC 司法辖区的信用与抵押净额结算 Layer2。以 Jurisdiction/Entity/Account（J/E/A）结构组织，普通支付与互换在本地更新账户，由辖区层执行注册、抵押、结算与争议；Runtime 作为单一写入者，采用确定性状态机转换并在 WAL 持久化后才进行外部 I/O。含可独立运行的 BrainVault 钱包派生模块。README 标注为草稿阶段，主网发布有验收门槛，使用 Bun 运行，AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- J/E/A 三层结构与 RCPAN 统一账户模型
- Runtime 单一写入者，确定性转换 + WAL 提交后才执行链上/网络 I/O
- BrainVault 独立内存硬钱包派生模块，可脱离 XLN 单独审计
- Solidity 合约测试与仓库验证门控（bun run check）

## 适用场景

- 构建跨辖区可验证的双边信用/抵押结算通道
- 审计确定性状态机的财务转换与提交边界
- 独立运行并审计 BrainVault 钱包派生模块

## 场景标签

 · 领域:区块链/金融基础设施

## 证据(README 行号)

> L35: ├── core/             deterministic Runtime, Entity, Account, and boundaries
> L101: - Jurisdiction enforces registration, collateral, settlement and disputes;

## 星数曲线

```mermaid
xychart-beta
    title "xlnfinance/xln 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-24 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 low · 依据 README sha `13852a866de6` · [字段定义](../../DATASET.md)*
